import uuid
from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id=None, fabric=None, condition=None):
        self.id = uuid.uuid4().int if id is None else id
        self.fabric = "Unknown" if fabric is None else fabric
        self.condition = 0 if condition is None else condition
    def __str__(self):
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."

