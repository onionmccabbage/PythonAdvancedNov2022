import json

class Item():
    '''This class encapsulates items that have a name and a cost
    Name is a string, cost is a positive float'''
    def __init__(self, name, cost):
        self.name = name # this will call the setter method for name
        self.cost = cost
    @property
    def name(self): # here is the getter method (accessor)
        return self.__name # return the name-mangled property
    @name.setter
    def name(self, new_name): # here is the setter method (mutator)
        if type(new_name) == str:
            self.__name = new_name
        else:
            raise Exception('Name must be a string')
    @property
    def cost(self):
        return self.__cost
    @cost.setter
    def cost(self, new_cost):
        if type(new_cost)==float and new_cost >=0:
            self.__cost = new_cost
        else:
            raise Exception('cost must be a positive float')

# we can write a class to encode our 'Item' class
class ItemEncoder(json.JSONEncoder): # we inherit from the built-in JSON Encoder
    def default(self, obj): # here we override he built-in 'default' of JSONEncoder
        # check we are dealing with an instance of 'Item'
        if isinstance(obj, Item):
            return obj.__dict__ # every class will have an instinsic __dict__
        else:
            return json.JSONEncoder.default(self, obj) # just use the sdefault JSONEncoder method

def main():
    '''we need to store instances of 'item' as json '''
    z = Item('Zoe', 23.00)
    x = Item('Xante', 99.99)
    # can we ncode these as JSON?
    z_j = json.dumps(z, cls=ItemEncoder) # use our encoder class
    print(z_j) # does this work??
    # NB we could just serialize the __dict__ of ANY class
    x_j = json.dumps(x.__dict__)
    print(x_j)

if __name__ == '__main__':
    main()