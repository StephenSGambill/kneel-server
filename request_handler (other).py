import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from views import get_all_styles, get_all_items, get_all_metals, get_all_sizes, get_all_orders
from views import get_single_style, get_single_item, get_single_metal, get_single_size
from views import create_order, delete_order, update_order, get_single_order
from views import all, retrieve
from urllib.parse import urlparse

method_mapper = {
    "items": {
        "all": all,
        "single": retrieve
},
    "metals": {
        "all": all,
        "single": retrieve
},
    "orders": {
        "all": all,
        "single": retrieve
},
    "sizes": {
        "all": all,
        "single": retrieve
},
    "styles": {
        "all": all,
        "single": retrieve
    }
}


class HandleRequests(BaseHTTPRequestHandler):
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """

    def parse_url(self, path):
        url_components = urlparse(path) #various components broken into truple
        path_params = url_components.path.strip("/").split("/")
        query_param = url_components.query.split("&")
        
        resource = path_params[0]
        id = None

        try:
            id = int(path_params[1])
        except IndexError:
            pass
        except ValueError:
            pass

        return (resource, id, query_param)

    def do_GET(self):
        """Handles GET requests to the server """

        response = None
        (resource, id, query_param) = self.parse_url(self.path)
        response = self.get_all_or_single(resource, id, query_param)
        self.wfile.write(json.dumps(response).encode())

    def get_all_or_single(self, resource, id, query_param):
        if id is not None:
            response = method_mapper[resource]["single"](resource, id, query_param)
            if response is not None:
                self._set_headers(200)
            else: 
                self._set_headers(404)
                response = "not found"
        else:
            self._set_headers(200)
            response = method_mapper[resource]["all"](resource)
            
        return response

    def do_POST(self):
        """Handles POST requests to the server """
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)
        (resource, id) = self.parse_url(self.path)

        new_order = None

        if resource == "orders":
            if "metalId" in post_body and "sizeId" in post_body and "styleId" in post_body and "itemId" in post_body:
                new_order = create_order(post_body)
                self.wfile.write(json.dumps(new_order).encode())
            else:
                self._set_headers(400)
                message = {
                    "message": f'{"Metal is required" if "metalId" not in post_body else ""}{"Size is required" if "sizeId" not in post_body else ""}{"Style is required" if "styleId" not in post_body else ""}{"Item is require" if "itemId" not in post_body else ""}'
                }
                self.wfile.write(json.dumps(message).encode())


    def do_PUT(self):
        """Handles PUT requests to the server """
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)

        if resource == "orders":
            self._set_headers(405)
            message = {
                "message": "Updating an order is not allowed after it has been placed."}
            self.wfile.write(json.dumps(message).encode())

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


def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
