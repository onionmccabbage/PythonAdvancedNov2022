# double-ended queue
# we can profile the code using memory_profiler
# we may need to pip install memory_profiler
from memory_profiler import profile
import collections

@profile # we can decorate ANY function to get a performance profile
def someFn():
    my_deq = collections.deque('98765432')
    # what do we have?
    my_deq.append('1') # 987654321
    my_deq.appendleft('0') # 0987654321
    my_deq.pop() # 098765432
    my_deq.popleft() # 987565432
    print( type(my_deq), my_deq )


if __name__ == '__main__':
    someFn()