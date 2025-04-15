import uuid

class Item:
    def __init__(self, id=None, condition=0):
        self.id = uuid.uuid4().int if id is None else id
        self.condition = condition

    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."

    def condition_description(self):        
        if 0 <= self.condition < 1:
            return 'Poor Condition'
        elif self.condition < 2:
            return 'Fair Condition'
        elif self.condition < 3:
            return 'Good Condition'
        elif self.condition < 4:
            return 'Very Good Condition'
        elif self.condition <= 5:
            return 'New Condition'
        else:
            return 'Unknown Condition'