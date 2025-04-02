import uuid
from swap_meet.item import Item

class Decor(Item):
    def __init__(self, id=None, condition=None, width=None, length=None):
        super().__init__(id, condition)
        self.width = width if width is not None else 0 
        self.length = length if length is not None else 0 

    def __str__(self):
        return f"An object of type Decor with id {self.id}. It takes up a {self.width} by {self.length} sized space."
