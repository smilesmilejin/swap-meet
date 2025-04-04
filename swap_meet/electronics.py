from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, id=None, condition=None, type=None):
        super().__init__(id, condition)
        self.type = "Unknown" if type is None else type
    
    def __str__(self):
        return f"{super().__str__()} This is a {self.type} device."