import doctest

def nthpower(d, p):
    '''
    return the nth power of a number
    We can write doctest within the doc string
    >>> nthpower(4,3)
    64
    '''
    return d**p

def cubeIt(a, b):
    '''
    return all the cubes of numbers from a to b
    >>> cubeIt(3, 8)
    [27, 64, 125, 216, 343]
    >>> cubeIt(1, 11) # doctest:+ELLIPSIS
    [1, 8, ..., 1000]
    '''
    answers = []
    for i in range(a, b):
        answers.append( i**3 )
    return answers

if __name__ == '__main__':
    doctest.testmod(verbose=True)