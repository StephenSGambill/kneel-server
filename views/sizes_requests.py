import sqlite3
from models import Size




def get_all_sizes():
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        SELECT
            s.id,
            s.carets,
            s.price

        FROM Sizes s
        """
        )

        sizes = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            size = Size(
                row["id"],
                row["carets"],
                row["price"],
            )
            
            sizes.append(size.__dict__)

    return sizes

def get_single_size(id):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        SELECT
            s.id,
            s.carets,
            s.price
        FROM Sizes s
        WHERE s.id = ?
        """,
        (id,),
        )

        sizes = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            size = Size(
                row["id"],
                row["carets"],
                row["price"],
            )
            
            sizes.append(size.__dict__)

    return sizes

