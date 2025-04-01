from swap_meet.item import Item

class Vendor:   
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory 
    
    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if (not self.inventory) or (item not in self.inventory):
            return False
        self.inventory.remove(item)
        return item
    
    # Instance Method to Add to the Vendor Class:
    ################# Wave 2 - 2
    def get_by_id (self, id):
        for each_item in self.inventory:
            if id == each_item.id:
                return each_item
        
        return None
    
    ################### Wave 3 - 2
    def swap_items(self, other_vendor, my_item, their_item):
        if (my_item not in self.inventory) or (their_item not in other_vendor.inventory):
            return False

        self.remove(my_item)
        other_vendor.add(my_item)
        self.add(their_item)
        other_vendor.remove(their_item)
        return True
    
