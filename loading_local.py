# we will load some data from a local file
# in this case, it will be structured data in JSON format
import json # this is part of Python

def main():
    '''Load a local set of JSON data then print iteratively'''
    fin = open('todos.json', 'rt') # 'r' to read 't' for text (default)
    all_j = fin.read() # we read in the whole thing
    all_l = json.loads(all_j) # convert to structure
    all_j = json.dumps(all_l) # convert back to text
    print( type(all_l[0]) )   # we have a list of dictionaries
    # we can iterate over the list
    for i in range(0, 5): # or use length of the list
        print(all_l[i])

if __name__ == '__main__':
    main()