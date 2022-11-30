import sys # the system on which Python is running

class Redirect:
    '''
    This class will redirect output to a different stream
    Returns the original output stream when done
    '''
    def __init__(self, new_stdout):
        ''' receive a new output stream as new_stdout'''
        self.new_stdout = new_stdout
    def __enter__(self):
        '''the __enter__ method is invoked whenever this class or an instance of it is run'''
        self.orig_stdout = sys.stdout # remember what the output stream was
        sys.stdout = self.new_stdout  # switch the output steeam to whatever wasd passed in
    def __exit__(self, exc_type, exc_value, exc_traceback): # we MUST provide all four arguments
        '''the __exit__ method is invoked whenever this class or an instance of it stops'''
        sys.stdout = self.orig_stdout # switch the output stream back to what it was

if __name__ == '__main__':
    # what is the default sys.stdout?
    # print(sys.stdout)
    print('Initially the output stream is {}'.format(sys.stdout))
    with open('my_log.txt', 'a') as fobj: # we now have a file access object
        r = Redirect(fobj) # r is an instance of our class
        # with Redirect(fobj): # here we use the class directly
        with r: # here we use a class instance
            print('Output is now sent to the log via the file acess object. Default stream is now {}'.format(sys.stdout))
        # when we are done, our class calls __exit__ which returns the context
        print('back to the console')
