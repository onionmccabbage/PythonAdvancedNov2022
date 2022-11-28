# here we will declare a decorator with a specific purpose

def show_args(func): # decorators always take an icoming function
    '''This function will be used to decorate other functions
    This decorator will display all the incoming parameters of the decorated function
    '''
    # *args is the tuple of ALL positional arguments
    # **kwargs is th dictionary of ALL key-word arguments
    def my_fn(*args, **kwargs): 
        '''we can print out the passed-in arguments'''
        print(f'Running a function called {func.__name__}')
        print(f'The positional arguments are {args}')
        print(f'The key-word arguments are {kwargs}')
        # then we run the passed-in function
        return func(*args, **kwargs)
    return my_fn # NB here we are not actually invoking the function, just returning it

# see the decorator in use
# here is a trivial function
@show_args # here we apply our custom decorator to another function
def add_integers(a, b):
    '''return the sum of the two integer parameters'''
    return a+b

if __name__ == '__main__':
    # here we experiment with diffent kinds of arguments: positiona and key-word
    print( add_integers(4, 5) ) # we pass in positional arguments
    print( add_integers(a=13, b=27) ) # we pass in key-word arguments
    print( add_integers(20, b=99) ) # we pas a positional and a key-word argument
    # NB ALL positional arguments MUST appear before the key-word arguments