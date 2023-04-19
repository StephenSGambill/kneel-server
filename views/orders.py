import sqlite3
import json
from models import Order
from .metals_requests import get_single_metal
from .sizes_requests import get_single_size
from .styles_requests import get_single_style
from .items_requests import get_single_item


# ORDERS = [
#     {
#         "id": 1,
#         "metalId": 3,
#         "sizeId": 2,
#         "styleId": 3,
#         "itemId": 1,
#         "timestamp": 1614659931693
#     }
# ]


# def get_all_orders():
#     return ORDERS

def get_all_orders():
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute(
            """
        SELECT
            o.id,
            o.metal_id,
            o.size_id,
            o.style_id

        FROM [Order] o
            """)
        
        orders = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            order = Order(
                row["id"],
                row["metal_id"],
                row["size_id"],
                row["style_id"],
            )

            orders.append(order.__dict__)

    return orders


# def get_single_order(id):
#     ("hit")
#     requested_order = None
#     for order in ORDERS:
#         if order["id"] == id:
#             requested_order = order

#             order_metal_info = get_single_metal(requested_order["metalId"])
#             order["metal_type"] = order_metal_info["metal"]
#             order["metal_price"] = order_metal_info["price"]

#             order_size_info = get_single_size(requested_order["sizeId"])
#             order["size"] = order_size_info["carets"]
#             order["size_price"] = order_size_info["price"]

#             order_style_info = get_single_style(requested_order["styleId"])
#             order["style_type"] = order_style_info["style"]
#             order["style_price"] = order_style_info["price"]

#             order_item_info = get_single_item(requested_order["itemId"])
#             order["type"] = order_item_info["type"]
#             order["type_price"] = order_item_info["pricePoint"]

#             del order["metalId"]
#             del order["sizeId"]
#             del order["styleId"]
#             del order["itemId"]

#     return requested_order

def get_single_order(id):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute(
            """
        SELECT
            o.id,
            o.metal_id,
            o.size_id,
            o.style_id
        FROM [Order] o
        WHERE o.id = ?
        """,
            (id,),
        )

        data = db_cursor.fetchone()

        order = Order(
            data["id"],
            data["metal_id"],
            data["size_id"],
            data["style_id"]
        )

        return order.__dict__


# def create_order(order):
#     max_id = ORDERS[-1]["id"]
#     (ORDERS)
#     new_id = max_id + 1
#     order["id"] = new_id
#     ORDERS.append(order)

#     # Return the dictionary with `id` property added
#     return order

def create_order(new_order):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        INSERT INTO [Order]
            ( metal_id, size_id, style_id )
        VALUES
            ( ?, ?, ?);
        """,
            (
                new_order["metal_id"],
                new_order["size_id"],
                new_order["style_id"],
                
            ),
        )

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the order dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_order["id"] = id

    return new_order

# def update_order(id, new_order):
#     for index, order in enumerate(ORDERS):
#         if order["id"] == id:
#             ORDERS[index] = new_order
#             break

def update_order(id, new_order):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute(
            """
        UPDATE [Order]
            SET
                metal_id = ?,
                size_id = ?,
                style_id = ?
        WHERE id = ?
        """,
            (
                new_order["metal_id"],
                new_order["size_id"],
                new_order["style_id"],
                id,
            ),
        )

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True



# def delete_order(id):
#     order_index = -1
#     for index, order in enumerate(ORDERS):
#         if order["id"] == id:
#             order_index = index

#     if order_index >= 0:
#         ORDERS.pop(order_index)


def delete_order(id):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        DELETE FROM [Order]
        WHERE id = ?
        """,
            (id,),
        )
