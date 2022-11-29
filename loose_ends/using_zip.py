# in Python 'zip' is nothing to do with compression
# its much more like a zipper where the two sides interlock

# here are some collections
days   = ('mon', 'tue', 'wed', 'thu', 'fri') # 5 members
fruits = ['banana', 'orange', 'kiwi', 'durian'] # 4 members
drink  = ['coffee', 'tea', 'water', 'soya']

# zip lets us combine collections (shortest collection determines what gets zipped)
j = zip(days, fruits, drink)

print(j) # we have a zip object

# we can iterate over a zip object
for d, f, k in j:
    print(f'On {d} I ate {f} with {k}')