DATABASE = {
    "ITEMS": [
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
], 
    "METALS": [
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
], 
    "ORDERS": [
    {
        "id": 1,
        "metalId": 3,
        "sizeId": 2,
        "styleId": 3,
        "itemId": 1,
        "timestamp": 1614659931693
    },
    {
        "id": 2,
        "metalId": 2,
        "sizeId": 1,
        "styleId": 2,
        "itemId": 2,
        "timestamp": 1614659931693
    }
],
    "SIZES": [
    {
        "id": 1,
        "carets": 0.5,
        "price": 405
    },
    {
        "id": 2,
        "carets": 0.75,
        "price": 782
    },
    {
        "id": 3,
        "carets": 1,
        "price": 1470
    },
    {
        "id": 4,
        "carets": 1.5,
        "price": 1997
    },
    {
        "id": 5,
        "carets": 2,
        "price": 3638
    }
],
    "STYLES": [
    {
        "id": 1,
        "style": "Classic",
        "price": 500
    },
    {
        "id": 2,
        "style": "Modern",
        "price": 710
    },
    {
        "id": 3,
        "style": "Vintage",
        "price": 965
    }
]
}

def all(resource):
    RESOURCE =  resource.upper()
    return DATABASE.get(RESOURCE)   

def retrieve(resource, id, query_param):
    if resource.upper() == "ORDERS":
        order_info = next((order for order in DATABASE["ORDERS"] if order["id"] == id), None).copy()
        if query_param == ['']:
            order_info["metal"] = retrieve("METALS", order_info["metalId"], query_param)
            order_info["size"] = retrieve("SIZES", order_info["sizeId"], query_param)
            order_info["style"]  = retrieve("STYLES", order_info["styleId"], query_param)
            order_info["total"] = order_info["metal"]["price"] + order_info["size"]["price"] + order_info["style"]["price"]
        else:
            order_info[query_param[0]] = retrieve(query_param[0] +'s', order_info[f"{query_param[0]}Id"], query_param)
        return order_info
    else:
        return next((instance for instance in DATABASE[resource.upper()] if instance["id"] == id), None)    