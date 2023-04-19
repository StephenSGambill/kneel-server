import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from views import get_all_styles, get_all_items, get_all_metals, get_all_sizes, get_all_orders
from views import get_single_style, get_single_item, get_single_metal, get_single_size
from views import create_order, delete_order, update_order, get_single_order, update_metal


class HandleRequests(BaseHTTPRequestHandler):
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """

    def parse_url(self, path):
        path_params = path.split("/")
        resource = path_params[1]
        id = None

        try:
            id = int(path_params[2])
        except IndexError:
            pass
        except ValueError:
            pass
        return (resource, id)

    def do_GET(self):
        """Handles GET requests to the server """
        self._set_headers(200)

        response = {}

        (resource, id) = self.parse_url(self.path)

        if resource == "metals":
            if id is not None:
                response = get_single_metal(id)
                if response is None:
                    self._set_headers(404)
                    response = {
                        "message": "That metal is not currently in stock for jewelry"}
            else:
                response = get_all_metals()
        elif resource == "items":
            if id is not None:
                response = get_single_item(id)
                if response is None:
                    self._set_headers(404)
                    response = {
                        "message": "That item is not currently in stock for jewelry"}
            else:
                response = get_all_items()
        elif resource == "styles":
            if id is not None:
                response = get_single_style(id)
                if response is None:
                    self._set_headers(404)
                    response = {
                        "message": "That style is not currently in stock for jewelry"}
            else:
                response = get_all_styles()
        elif resource == "sizes":
            if id is not None:
                response = get_single_size(id)
                if response is None:
                    self._set_headers(404)
                    response = {
                        "message": "That size is not currently in stock for jewelry"}
            else:
                response = get_all_sizes()
        elif resource == "orders":
            if id is not None:
                response = get_single_order(id)
                if response is None:
                    self._set_headers(404)
                    response = {
                        "message": "That order was never placed, or was cancelled"}
            else:
                response = get_all_orders()
        else:
            response = []

        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        """Handles POST requests to the server """
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)
        (resource, id) = self.parse_url(self.path)

        new_order = None

        if resource == "orders":
            if "metal_id" in post_body and "size_id" in post_body and "style_id" in post_body:
                new_order = create_order(post_body)
                self.wfile.write(json.dumps(new_order).encode())
            else:
                self._set_headers(400)
                message = {
                    "message": f'{"Metal is required" if "metal_id" not in post_body else ""}{"Size is required" if "size_id" not in post_body else ""}{"Style is required" if "style_id" not in post_body else ""}'
                }
                self.wfile.write(json.dumps(message).encode())

        # response = {"payload": post_body}

    def do_PUT(self):
        """Handles PUT requests to the server """
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)
        (resource, id) = self.parse_url(self.path)
        success = False
    
        if resource == "metals":
            success = update_metal(id, post_body)
            self.wfile.write("".encode())
            
            if success: 
                self._set_headers(204)
            else:
                self._set_headers(404)

        elif resource == "orders":
            success = update_order(id, post_body)
            self.wfile.write("".encode())
            
        if success: 
            self._set_headers(204)
        else:
            self._set_headers(404)


    def do_DELETE(self):
        self._set_headers(204)

        (resource, id) = self.parse_url(self.path)

        if resource == "orders":
            delete_order(id)

        self.wfile.write("".encode())

    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()


# point of this application.
def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
