import sqlite3

def readDB():
    '''read back from our Zoo table'''
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    st = '''
        SELECT creature, count, cost FROM zoo
    '''
    try:
        curs.execute(st)
        conn.commit() # not needed - no changes made
        # now we can use our cursor to fetch the data
        rows = curs.fetchall()
    except Exception as err:
        print(err)
    finally:
        conn.close()
    # we can iterate over the returned data
    for animal in rows:
        print('we have {1} {0} each costing {2:0.2f}'.format(animal[0], animal[1], animal[2]))

if __name__ == '__main__':
    readDB()