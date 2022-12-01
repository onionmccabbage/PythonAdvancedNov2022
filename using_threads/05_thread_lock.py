from threading import Lock
import time
import timeit
import random
import sys
from memory_profiler import profile

@profile(precision=4)
def main(): # we will explore acquire and release of locks
    lock = Lock() # we now have a lock we can use
    lock.acquire() # we have exclusive access to this lock
    try:
        for i in range(1, 50):
            time.sleep(random.random()*0.1)
            print(f'{i}')
    except Exception as err:
        print(err)
    finally:
        pass
        lock.release() # always make sure we release!!!

    # alternative syntax for lock acquire and release
    # with lock:# the lock will be automatically released when the 'with' ends
    #     for i in range(1, 50):
    #         time.sleep(random.random()*0.1)
    #         print(f'{i}')
    # the lock is released so other threads can access the resources

if __name__ == '__main__':
    start = timeit.default_timer()
    main()
    end = timeit.default_timer()
    print(f'it took {end-start}')