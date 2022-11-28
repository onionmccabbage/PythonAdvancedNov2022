# we can use the built-in urllib or the simpler requests library
# from urllib import request # this is ok but usually we would use another library

# if we dont already have the requests library
# then we need to pip install requests or conda install request
import requests
import sys # this gives acces to the current operating system

# a function to make an API call and retrieve some data
def makeCall(cat='users', id=3): # aruments with sensible defaults
    ''' retrieve data from an API end-point'''
    url = 'https://jsonplaceholder.typicode.com' # this returns JSON data
    # url = 'https://nonsuch.com' # this returns JSON data
    # cat = 'users' # which category
    # id = 3 # which user ID
    # it's always a good idea to use try-except 
    try:
        response = requests.get( f'{url}/{cat}/{id}' ) # build the end-point URL
        print(type(response))
        print(response)
        # we can parse the JSON from the response
        response_j = response.json() # this is built in to the requests library
        print(response_j)
    except Exception as err:
        print(f'something went wrong {err}')

if __name__ == '__main__':
    # check to see if any additional system argument variables have been pased in 
    if len(sys.argv) > 1: # greater than one - rmeember the module name is ALWAYS passed in
        category = sys.argv[1] # sys.argv counts from zero
        id       = sys.argv[2]
        makeCall(category, id)
    else:
        # call our function - we can pass in system arguments
        makeCall('photos', 77)
