import uuid

class Item:
    def __init__(self, id=None, condition=None):
        self.id = uuid.uuid4().int if id is None else id
        self.condition = 0 if condition is None else condition
    
    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def condition_description(self):    
        conditions = {
            0: 'Poor Condition',
            1: 'Fair Condition',
            2: 'Good Condition',
            3: 'Very Good Condition',
            4: 'Excellent Condition',
            5: 'New Condition'
        }
        
        return conditions[self.condition]