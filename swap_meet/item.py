import uuid
################## Wave 2
class Item:
    def __init__(self, id=None, condition=None):
        self.id = uuid.uuid4().int if id is None else id
        ############### Wave 5
        self.condition = 0 if condition is None else condition
    def get_category(self):
        return self.__class__.__name__
    
    ################## Wave 3
    def __str__(self):
        return f"An object of type Item with id {self.id}."
    
    def condition_description(self):
        if self.condition == 0:
            return 'Poor Condition'
        elif self.condition == 1:
            return 'Fair Condition'
        elif self.condition == 2:
            return 'Good Condition'
        elif self.condition == 3:
            return 'Very Good Condition'
        elif self.condition == 4:
            return 'Excellent Condition'
        elif self.condition == 5:
            return 'New Condition'