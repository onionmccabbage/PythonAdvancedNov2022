# here two instances of a class will battle with 'counter' resources
from threading import Lock, Thread

lock = Lock()
count1 = 0
count2 = 0

class MyClass:
    def __call__(self, name):
        global loc, count1, count2
        for i in range(0,20): # nb the value of 'i' will be unique to each thread
            count1 += 1
            print(f'{name} c1: {count1}') #count1 is NOT being locked
        lock.acquire() # we make sure we are 'thread safe'
        for i in range(0,20):
            count2 += 1
            print(f'{name} c2: {count2}') #count2 is being locked
        lock.release()

def main():
    m1 = MyClass()
    m2 = MyClass()
    t1 = Thread(target=m1, args=('m1',))
    t2 = Thread(target=m2, args=('m2',))
    t1.start()
    t2.start()
    t1.join()
    t2.join()



if __name__ == '__main__':
    main()