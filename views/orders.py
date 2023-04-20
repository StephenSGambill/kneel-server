import sqlite3
import json
from models import Order
from models import Metal
from models import Size
from models import Style
from .metals_requests import get_single_metal
from .sizes_requests import get_single_size
from .styles_requests import get_single_style
from .items_requests import get_single_item



def get_all_orders():
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute(
            """
        SELECT
            o.id,
            o.metal_id,
            m.metal,
            m.price,
            o.size_id,
            s.carets,
            s.price,
            o.style_id,
            st.style,
            st.price

        FROM Orders o
        JOIN Metals m ON m.id = o.metal_id
        JOIN Sizes s ON s.id = o.size_id
        JOIN Styles st ON st.id = o.style_id
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

            metal = Metal(
                row["id"],
                row["metal"],
                row["price"],
            )

            size = Size(
                row["id"],
                row["carets"],
                row["price"]

            )

            style = Style(
                row["id"],
                row["style"],
                row["price"]
            )

            order.metal = metal.__dict__
            order.size = size.__dict__
            order.style = style.__dict__
            orders.append(order.__dict__)

    return orders



def get_single_order(id):
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
        FROM Orders o
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



def create_order(new_order):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        INSERT INTO Orders
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

        id = db_cursor.lastrowid

        new_order["id"] = id

    return new_order


def update_order(id, new_order):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute(
            """
        UPDATE Orders
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


def delete_order(id):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        DELETE FROM Orders
        WHERE id = ?
        """,
            (id,),
        )
