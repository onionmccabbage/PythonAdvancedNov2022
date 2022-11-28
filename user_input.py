# when the user enters data at the console it is ALWAYS a string of text

def getInfo():
    value = input('Please enter a value ')
    # what is the type of the user input?
    print( f'The type of data you entered is {type(value)}' )
    # can we convert this to an integer
    value_int = int(float(value)) # careful - always make a float then an int
    print(f'Value {value} can be converted to {type(value_int)} of {value_int}')

if __name__ == '__main__':
    getInfo()
