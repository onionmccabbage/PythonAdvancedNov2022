# Python uses generators and comprehension
r = range(3, 35, 4) # start, stop-before, step - the values do not persist in memory, they are yielded
# we can make our own generator from this range
g = ( i*i for i in r ) # round-brackets: this will generate all the squares of members in the range
print(type(g)) # we have a generator object
l = [ i*i for i in r ] # this is not a generator
print(type(l)) # ... it is a list. All the values exist in memory

# we can write a custom generator
def byteGen(start, stop_before):
    '''this is a custom generator to make bytes out of positive integers between two values'''
    s = start
    while s < stop_before:
        # yield instead of return
        yield bytes(s) # yield makes this function into a generator
        s += 1 # increment by 1

if __name__ == '__main__':
    # we ned an instance of our custom generator
    b = byteGen(1, 255)
    print( type(byteGen) )
    print( b.__next__() ) # yield the next value from our generator
    # we should be able to iterate over the values generated
    for v in b:
        print(v, end=', ')
        


