#iter is built in to python
l = [False, 7, 'text', (5,4,3,2)]
l_iter = iter(l)  # create an iter object from the list

print( l_iter.__next__(), end=', ' ) # False
print( l_iter.__next__(), end=', ' ) # 7
print( l_iter.__next__(), end=', ' ) # 'text'
print( l_iter.__next__(), end=', ' ) # the tuple
print( l_iter.__next__(), end=', ' ) # oops - nothing left to yield!!