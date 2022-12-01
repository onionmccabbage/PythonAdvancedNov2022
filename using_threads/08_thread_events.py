# when a thread is started, it runs to cmpeltion then joins the main thread
# the only way to communicate is via thread events
from threading import Thread, Event
import time

event = Event()

class MyClass():
    def __call__(self, name):
        global event
        print(f'{name} is waiting for a thread event...')
        event.wait() # this thread will not proceed until the event occurs
        print(f'{name} has received the event and is continuing execution')
        event.set()

if __name__ == '__main__':
    m1 = MyClass()
    t1 = Thread(target=m1, args = ('t1',))
    t1.start()
    # wait a few seconds, then send an event message to our thread
    time.sleep(5) # the main threaad sleeps for five seconds
    event.set() # here we trigger the event instance
    t1.join() # join AFTER setting the event!!
    event.wait()
    print('Main thread continues after the child thread event occurred')