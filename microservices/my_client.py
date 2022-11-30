import socket
import sys

def my_client():
    '''this is an http client'''
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # try to connect to our server
    param_t = ('localhost', 9874) # server and port
    sock.connect( param_t )
    # send a message to the server
    msg = 'hello is it coffee time?'
    sock.send( msg.encode() ) # all http MUST be encoded
    # handle any response from the server
    res = sock.recv(1024)
    print(res)
    sock.close() # tidy up


if __name__ == '__main__':
    my_client() # invoke the client