from .metals_requests import get_single_metal
from .sizes_requests import get_single_size
from .styles_requests import get_single_style
from .items_requests import get_single_item

ORDERS = [
    {
        "id": 1,
        "metalId": 3,
        "sizeId": 2,
        "styleId": 3,
        "itemId": 1,
        "timestamp": 1614659931693
    }
]


def get_all_orders():
    return ORDERS


def get_single_order(id):
    print("hit")
    requested_order = None
    for order in ORDERS:
        if order["id"] == id:
            requested_order = order

            order_metal_info = get_single_metal(requested_order["metalId"])
            order["metal_type"] = order_metal_info["metal"]
            order["metal_price"] = order_metal_info["price"]

            order_size_info = get_single_size(requested_order["sizeId"])
            order["size"] = order_size_info["carets"]
            order["size_price"] = order_size_info["price"]

            order_style_info = get_single_style(requested_order["styleId"])
            order["style_type"] = order_style_info["style"]
            order["style_price"] = order_style_info["price"]

            order_item_info = get_single_item(requested_order["itemId"])
            order["type"] = order_item_info["type"]
            order["type_price"] = order_item_info["pricePoint"]

            del order["metalId"]
            del order["sizeId"]
            del order["styleId"]
            del order["itemId"]

    return requested_order


def create_order(order):
    max_id = ORDERS[-1]["id"]
    print(ORDERS)
    new_id = max_id + 1
    order["id"] = new_id
    ORDERS.append(order)

    # Return the dictionary with `id` property added
    return order


def update_order(id, new_order):
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            ORDERS[index] = new_order
            print(new_order)
            break


def delete_order(id):
    order_index = -1
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            order_index = index

    if order_index >= 0:
        ORDERS.pop(order_index)
