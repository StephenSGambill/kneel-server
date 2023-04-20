import sqlite3
from models import Item



def get_all_items():
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute(
            """
        SELECT
            i.id,
            i.type,
            i.price
        FROM  Items i
            """)
        
        items = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            item = Item(
                row["id"],
                row["type"],
                row["price"],
            )

           
            items.append(item.__dict__)

    return items


def get_single_item(id):
     with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute(
            """
        SELECT
            i.id,
            i.type,
            i.price
        FROM  Items i
        WHERE i.id = ?
            """,
            (id,),
            )
        
        items = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            item = Item(
                row["id"],
                row["type"],
                row["price"],
            )

           
            items.append(item.__dict__)

        return items


