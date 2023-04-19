import sqlite3
import json
from models import Metal

METALS = [
    {
        "id": 1,
        "metal": "Sterling Silver",
        "price": 12.42
    },
    {
        "id": 2,
        "metal": "14K Gold",
        "price": 736.4
    },
    {
        "id": 3,
        "metal": "24K Gold",
        "price": 1258.9
    },
    {
        "id": 4,
        "metal": "Platinum",
        "price": 795.45
    },
    {
        "id": 5,
        "metal": "Palladium",
        "price": 1241.0
    }
]


# def get_all_metals():
#     return METALS

def get_all_metals():
    # Open a connection to the database, with conn as the variable
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        SELECT
            m.id,
            m.metal,
            m.price

        FROM Metal m
        """
        )

        metals = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            metal = Metal(
                row["id"],
                row["metal"],
                row["price"],
            )
            
            metals.append(metal.__dict__)

    return metals


# def get_single_metal(id):
#     requested_metal = None

#     for metal in METALS:
#         if metal["id"] == id:
#             requested_metal = metal

#     return requested_metal

def get_single_metal(id):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute(
            """
        SELECT
            m.id,
            m.metal,
            m.price
            
        FROM Metal m
        WHERE m.id = ?
        """,
            (id,),
        )

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        metal = Metal(
            data["id"],
            data["metal"],
            data["price"],
        )

        return metal.__dict__

def update_metal(id, new_metal):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute(
            """
        UPDATE Metal
            SET
                metal = ?,
                price = ?
        WHERE id = ?
        """,
            (
                new_metal["metal"],
                new_metal["price"],
                id,
            ),
        )

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True
