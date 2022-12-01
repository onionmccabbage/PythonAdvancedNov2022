import time # time simply measures a moment in time
import timeit
from functools import reduce

# cProfile is a profiling tool for python
# NB python is written in 'C'
# to invoke cProfile:
# python -m cProfile -o profiling_output fib.py
# this will record:
# number of calls, total time, timer per call, cumulative times

# the fibonacci series can take a long time to calculate
def fib(n):
    '''create the fibonacci series up to n'''
    if n<=1:
        return 1
    else:
        return ( fib(n-1)+fib(n-2) ) # self-reference

def util(a,b):
    return a+b

def fib2(n):
    seq = (0, 1)
    for _ in range(2, n+1):
        # lambda is a function literal - when we only need the function here (not elsewhere)
        seq += ( reduce( lambda a,b: a+b, seq[-2:] ), )  # e.g. (0, 1, 3, 5, 7, 13, 20, 33)
        # seq += ( reduce( util, seq[-2:] ), )  # e.g. (0, 1, 3, 5, 7, 13, 20, 33)
    return seq[n]

if __name__ == '__main__':
    start = time.time()
    s = timeit.default_timer() # much more accurate
    n=30 # careful!!!
    result = fib2(n) # fib is waaaay slower than fib2
    end = time.time()
    e = timeit.default_timer()
    duration = end-start
    d = e-s # using timeit
    print(f'Fibonacci up to {n} is {result} it took {duration} seconds or more accurately {d}')
