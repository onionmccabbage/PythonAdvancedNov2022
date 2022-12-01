from threading import Thread
import time 
import sys
import random

# declare a class which inherits from Thread
class MyThread(Thread):
    '''we override the 'run' method of the Thread access class'''
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name
    def run(self):
        '''this method is invoked when the thread is started'''
        for i in range(1,50):
            time.sleep(random.random()*0.1)
            print(self.name)

def main():
    m1 = MyThread('m1')
    m2 = MyThread('m2')
    m1.start() # this invokes the 'run' method
    m2.start()
    m1.join()
    m2.join()
    print('all done')

if __name__ == '__main__':
    main()