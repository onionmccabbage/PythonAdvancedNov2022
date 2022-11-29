# this utility will populate our db with many creatures
import sqlite3

def populateDb():
    '''
    Pass parameters into the DB for each new creature'''
    creatures_t = ( # normally this comes from JSON or API etc.
        {'creature':'Albatros', 'count':1,      'cost':120.99},
        {'creature':'Bear',     'count':5,      'cost':323.56},
        {'creature':'Carp',     'count':120,    'cost':87.00},
        {'creature':'Deer',     'count':121,    'cost':12.99},
        {'creature':'Elk',      'count':7,      'cost':73.47},
    )
    # 'conn' is the db access object (not the actual DB)
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    # we use ? to inject parameters into SQL statement
    st = '''
    INSERT INTO zoo
    VALUES (?, ?, ?)
    '''
    # iterate over the creaturs tuple to inject each creature into the statement
    for item in creatures_t:
        try:
            # we should check the values being inserted (sanitize)
            if type(item['creature']==str and item['creature'] != ''):
                n = item['creature']
            else:
                raise Exception('Name must be a non-empty string')
            if (type(item['count'])==int and item['count'] >= 0):
                c = item['count']
            else:
                raise Exception('count must be a positive integer')
            if (type(item['cost'])==float and item['cost'] >= 0):
                co = item['cost']
            else:
                raise Exception('cost must be a positive float')
            # use the sanitized values to inject into our SQL statement
            curs.execute(st, (n, c, co))
            conn.commit() # commit the changes
        except Exception as err:
            print(err)
    # tidy up
    conn.close() # we dont need the access object any longer


if __name__ == '__main__':
    populateDb()