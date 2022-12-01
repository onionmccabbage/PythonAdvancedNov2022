from threading import Thread, Lock
import time
import random
import sys

# we can declare some global values
counter = 0 # this will be a shared resource - could be a file access, db access....
lock = Lock()

# two threads will work on the counter. One will increment it, the other will decrmenet it
def workerA():
    global counter # the counter variable is now available within this function
    lock.acquire()
    try:
        while counter <100:
            counter += 1
            print(f'A increments counter to {counter}')
    except Exception as err:
        print(err)
    finally:
        lock.release()

def workerB():
    global counter # the counter variable is now available within this function
    lock.acquire()
    try:
        while counter >-100:
            counter -= 1
            print(f'B decrements counter to {counter}')
    except Exception as err:
        print(err)
    finally:
        lock.release()

def main():
    thread1 = Thread(target=workerA)
    thread2 = Thread(target=workerB)
    thread2.start()
    thread1.start()
    thread1.join()
    thread2.join()

if __name__ == '__main__':
    main()