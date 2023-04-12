ITEMS = [
    {
        "id": 1,
        "type": "Ring",
        "pricePoint": 1
    },
    {
        "id": 2,
        "type": "Earring",
        "pricePoint": 2
    },
    {
        "id": 3,
        "type": "Necklace",
        "pricePoint": 4
    }
]


def get_all_items():
    return ITEMS


def get_single_item(id):
    requested_item = None

    for item in ITEMS:
        if item["id"] == id:
            requested_item = item

    return requested_item
