import sqlite3
from models import Style


def get_all_styles():
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        SELECT
            s.id,
            s.style,
            s.price

        FROM Styles s
        """
        )

        styles = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            style = Style(  
                row["id"],
                row["style"],
                row["price"],
            )
            
            styles.append(style.__dict__)

    return styles

def get_single_style(id):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        SELECT
            s.id,
            s.style,
            s.price
        FROM Styles s
        WHERE s.id = ?
        """,
        (id,),
        )

        styles = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            size = Style(
                row["id"],
                row["style"],
                row["price"],
            )
            
            styles.append(size.__dict__)

    return styles