# explore args and kwargs

def fn(x='', y=True, z=(3,)):
    '''sample function'''


def otherFn( *args, **kwargs ): # args and kwargs are the conventional names 
    '''ALL functions will ALWAYS have 
    a tuple of positional arguments 
    and a dictionary of keyword argument'''
    print(*args, *kwargs ) # theasterisk will unpack the values

# Python has no 'overload' concepts
def getDBquery(*args):
    # if there are NO args, just retreive from the DB
    if len(args)==0:
        '''carry out code to retrieve all data from db'''
    if len(args)==1:
        '''use this single argumemt as a parameter in an SQL statement'''
    if len(args)==2:
        '''...'''

if __name__ == '__main__':
    # positional arguments - their position determines their allocation
    fn( 'here is a value for x', 345625736, {}  )
    fn() # this will allow the defaults to be in action
    # keyword arguments explicitly give their keyword assignment
    fn(z=[]) # use defaults for x and y but override the value of z
    # NB positionals MUST come before any keword args
    fn(7, y = False) # 7 is positional, y=False is a keyword arg
    otherFn(5,7,9,4,2,8,[],{}, (3,)) # loads of args
    otherFn(f=5,g=7,q=9,xy=4,n=2,w=8,p=[],a={}, kkkkk=(3,)) # loads of args


