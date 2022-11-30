import socket

def my_server():
    '''
    This service will echo any request back to the client
    (having first capitalized the request body)
    '''
    # we need to set socket parameters
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    param_t = ('localhost', 9874) # server address and port
    server.bind(param_t) # set our server parameters
    # begin listening for request
    server.listen(4) # handle up to 4 concurrent requests (all others will be queued)
    print(f'Server is listening on {param_t[0]} port {param_t[1]}')
    while True: # keep our server running
        # when a request is made, we need to handle it
        (client, addr) = server.accept() # unpacking the request
        print(client, addr)
        # read any data from the client
        buf = client.recv(1024) # read just the first 1024 bytes from the client
        print(f'Server received {buf}')
        # decide what to do about this request - in this case send back ALL_CAPS
        resp = buf.upper()
        client.send(resp)
        break

if __name__ == '__main__':
    my_server() # invoke our server