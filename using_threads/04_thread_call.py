from threading import Thread
import time
import random
import sys

#create a callable class
class MyClass: # NB this is NOT a Thread
    def __call__(self, name): # we can call this method to make a thread
        for i in range(1, 50):
            time.sleep(random.random()*0.1)
            print(name)

if __name__ == '__main__':
    m1 = MyClass()
    m2 = MyClass()
    # call our callable class instances
    t1 = Thread(target=m1,args=('t1',))
    t2 = Thread(target=m1,args=('t2',))
    # we may need ot manage these threads collectively
    my_threads = [t1, t2] # or a tuple
    # start all our threads
    for t in my_threads:
        t.start()
    # alter starting all the threads, we then join all our threads
    for t in my_threads:
        t.join()