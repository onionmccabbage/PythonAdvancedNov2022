# Python has a context manager
import sys
from contextlib import contextmanager # this can be used to decorate other functions

@contextmanager # this enabled context switching within our function
def stdout_redirect(new_stdout):
    '''This function can redirect the output stream'''
    orig_stdout = sys.stdout # remember what the previous context was
    sys.stdout  = new_stdout # switch context
    yield # this will yield the next available object to be written to the output stream
    sys.stdout  = orig_stdout # return the context to what it was

def main():
    with open('my_log.txt', 'a') as fobj:
        with stdout_redirect(fobj):
            print('''Here are several lines that will be sent to the log
Each line is redirected by our context manager''')
            print('this text also gets yielded to the file access object')
        print('back to the original output stream')

if __name__ == '__main__':
    main()