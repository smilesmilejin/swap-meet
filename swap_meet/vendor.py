from swap_meet.item import Item

class Vendor:   
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory 
    
    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item
    
    def get_by_id (self, id):
        for each_item in self.inventory:
            if id == each_item.id:
                return each_item
        
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if (my_item not in self.inventory) \
            or (their_item not in other_vendor.inventory):
            return False

        self.remove(my_item)
        other_vendor.add(my_item)
        
        self.add(their_item)
        other_vendor.remove(their_item)

        return True
    
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        
        self_first = self.inventory[0]
        other_vendor_first = other_vendor.inventory[0]
        
        return self.swap_items(other_vendor,self_first, other_vendor_first)


    def get_by_category(self, category):
        return [item for item in self.inventory if item.get_category() == category]

    def get_best_by_category(self,category):
        items_in_category = self.get_by_category(category)

        return max(items_in_category, key = lambda item: item.condition, default=None)

    # Method 1
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        vendor_wanted = other_vendor.get_best_by_category(my_priority)
        other_vendor_wanted = self.get_best_by_category(their_priority)

        if (not vendor_wanted) or (not other_vendor_wanted):
            return False
        
        self.swap_items(other_vendor, other_vendor_wanted, vendor_wanted)

        return True
    
    ## Method 2 Use Swap_items to return True or False
    # def swap_best_by_category(self, other_vendor, my_priority, their_priority):
    #     vendor_wanted = other_vendor.get_best_by_category(my_priority)
    #     other_vendor_wanted = self.get_best_by_category(their_priority)

    #     return self.swap_items(other_vendor, other_vendor_wanted, vendor_wanted)
