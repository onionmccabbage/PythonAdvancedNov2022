# there is a collection called named tuples
from collections import namedtuple

# imagine a task named-tuple
task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
# named tuples allow default values in case of absent members
task.__new__.__defaults__ = (None, None, False, None)

# define some tests for our Task named tuple
def test_defaults():
    t = task() # a copy/instance of our task object
    s = task(None, None, False, None)
    assert t==s # here is a pytest assertion This is a shallow check

def test_member_access():
    t=task('finish doing stuff', 'Grace') # leave the remaining defaults
    assert t.summary == 'finish doing stuff'
    assert t.owner   == 'Grace'
    assert (t.done, t.id) == (False, None)
    

if __name__ == '__main__':
    # t0 = task('talk about named tuples', 'td', False, 0)
    # t1 = task() # use the defaults
    # print(t0, t1)
    test_defaults() # the test pass silently
    test_member_access()