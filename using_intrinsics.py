# there are many useful intrinsics built in to python
# we can access them using __

class TopLevel():
    def __init__(self):
        pass # do nothing !!

class Derived(TopLevel):
    '''this class is derived from the TopLevel class'''
    def __init__(self):
        super().__init__() # call the initializer of the parent class
    def __str__(self): # we override the default 'print' capability
        return 'instance of the derived class'

if __name__ == '__main__':
    t = TopLevel()
    d = Derived()
    print(d)
    # we can examine some of the intrinsic members of our class instances
    print(f'Class name is {Derived.__name__}')
    print(f'Class docstring is {Derived.__doc__}')
    print(f'Class dictionary is {Derived.__dict__}') # all members of this class
    print(f'Class bases are {Derived.__bases__}') # all clases we inherit from