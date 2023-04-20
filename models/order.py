class Order():
    """Class that defines the properties for a style"""

    def __init__(self, id, metal_id, size_id, style_id):
        self.id = id
        self.metal_id = metal_id
        self.metal = None
        self.size_id = size_id
        self.size = None
        self.style_id = style_id
        self.style = None
