# here we can implement our abstract class
# we will write concrete shaoe classes
from a import AbstractShape

# ways to declare a class
class doobiedoobie: # implicitly inherit from 'object'
    pass
class ooblywoobly():# implicitly inherit from 'object'
    pass
class onlywooblydfp(object):# explicitly inherit from 'object'
    pass

class Shape(AbstractShape):
    def __init__(self, name):
        # shape_name LOOKS like a property - actually it is get/set methods
        self.shape_name = name # calls the SETTER method
    def __str__(self): # __str__ overrides the built-in 'print' method
        # return(f'This shape has the name {self.shape_name}')
        return('This shape has the name {}'.format(self.shape_name))
    @property # propertiues can take a getter and a setter
    def shape_name(self): # we ONLY need 'self' for a getter
        # here we GET the value of the name
        return self.__shape_name # __ is for name-mangling - makes the property hard to access directly
    @shape_name.setter
    def shape_name(self, new_name):
        # here we SET the value of the name
        if type(new_name) == str and new_name != '':
            self.__shape_name = new_name
        else:
            self.__shape_name = 'default' # we could raise an exception

if __name__ == '__main__':
    # we can create instances of our concrete class
    sq = Shape('square')
    print(sq.shape_name) # access the GETTER method as if it was just a property
    print(sq) # access the __str__ method
    tr = Shape('triangle')