# functional programming avoids classes
# pure functional programming: map, filter and reduce
from functools import reduce

def squareIt(x):
    '''return the square of a value'''
    return x*x

def addThem(x, y):
    '''return the two values added together'''
    return x+y

def isOdd(n):
    '''return True or False depending if the value of n is Odd or Even'''
    return n%2 !=0 # True of Odd, False if Even

if __name__ == '__main__':
    # we need to list all the squares of numbers in a range
    squares_list = ( map(squareIt, range(1,12)) ) # start at 1, stop-before 12
    print(f'The next square result is {squares_list.__next__()}') # the next value of the map object
    print(f'The next square result is {squares_list.__next__()}') # 4
    print(f'The next square result is {squares_list.__next__()}') # 9
    # we can choose to iterate over our map object
    for result in squares_list:
        print(f'The next square is {result}')

    # we can use filter to return only values filtered by a function
    odd_list = ( filter( isOdd, range(1,28) ) ) # start at 1, stop-before 28
    # we can persist the filter results in memory
    odd_tuple = tuple(odd_list) # we now have a tuple in memory
    odd_list = ( filter( isOdd, range(1,28) ) ) # re-populate our filter object
    print(odd_list.__next__() ) # 1 NB map and filter objects become exhausted when all their members have been used
    print(odd_list.__next__() ) # 3
    print(odd_list.__next__() ) # 5
    print(odd_list.__next__() ) # 7
    # or iterate over them
    for odd in odd_list:
        print(f'The next odd number is {odd}')
    
    # there is also a 'reduce' method (needs to be imported)
    # reduce will take a series of values and cumulatively apply a function
    # reduce ends up returning a SINGLE value
    r = reduce( addThem, odd_tuple )
    print(f'The total of all the odd numbers in the tuple is {r}')

