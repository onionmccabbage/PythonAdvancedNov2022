# threads let us run code concurrently
# all threads share the SAME instance of Python
# but they have their own memory values
import time
import random
from threading import Thread # this is the thread access object
import timeit

def myFunc(name):
    for i in range(1, 50):
        time.sleep(random.random()*0.1) # sleep for 0-0.1 second
        print(name) #, end=', ')

if __name__ == '__main__':
    # run the function on several threads
    start = timeit.default_timer()
    thread1 = Thread(target=myFunc, args=('t1',)) # positional arguments must be a tuple
    thread2 = Thread(target=myFunc, kwargs={'name':'t2'}) # keyword arguments must be in a dictionary
    # remember this module is already running in its own thread
    thread1.start() # this runs on its own thread
    thread2.start()
    thread1.join() # good practice to join other threads as early as possible
    thread2.join()
    end = timeit.default_timer()
    print(f'threading took {end-start} seconds')
    # what if we did this sequentially
    start = timeit.default_timer()
    myFunc('s1')
    myFunc('s2')
    end = timeit.default_timer()
    print(f'sequentially took {end-start} seconds')
    print('all done')