# here we will make use of our custom decorator
from custom_decorator import show_args

@show_args
def trivial(a=0, b=0, c=1): # they have default values
    return (a-b)**c

if __name__ == '__main__':
    print( trivial(3,2,1) ) 
    print( trivial(3,c=2,b=1) ) 
    print( trivial() ) # use the defaults
    print( trivial(c=3, b=9) ) 