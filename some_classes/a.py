# abstract base classes
# these bring a level of rigour to our code - helping us remember to implement stuff
from abc import ABCMeta, abstractmethod

class AbstractShape(): # this is going to be our abstract base class
    '''Abstract Classes do not implement any detail - they are abstractions'''
    @abstractmethod # remember the '@' is a decorator
    # we are going to always override the built-in __str__ method
    def __str__(self): # remember all class methods MUST take 'self'
        pass # we never put any detail into an abstract method
    @property  #the shape_name will b a property of the concrete classes
    @abstractmethod
    def shape_name(self, new_name):
        pass # no concrete implementation - this is abstraction

if __name__ == '__main__':
    # when you run a module, Python ALWAYS assigns the name __main__ to that module
    print(f'This module is given the name {__name__} by Python')