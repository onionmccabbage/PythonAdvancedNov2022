import sqlite3

def custom_readDB():
    '''Ask the user which creature they woud like to retrieve'''
    whichCreature = input('Which creature? ')
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    # we use a 'where' clause in the SQL to retrieve specific data
    # st = '''
    #     SELECT creature, count, cost FROM zoo
    #     WHERE creature="{}"
    # '''.format(whichCreature) # we realy should sanitize this user-entered data
    st = '''
        SELECT creature, count, cost FROM zoo
        WHERE creature LIKE "%{}%"
    '''.format(whichCreature)
    # percent in SQL can stand for any character
    # LIKE "s%" means anything begining 's'
    # LIKE "%s" means anything ENDING in 's'
    # LIKE "%s%" means anything CONTAINING 's'
    try:
        curs.execute(st)
        rows = curs.fetchall()
    except Exception as err:
        print(err)
    finally:
        conn.close()
    # iterate over the returned data
    for animal in rows:
        print('we have {1} {0} each costing {2:.2f}'.format(animal[0], animal[1], animal[2]))
    

# SQL Injection problems
# if the user enters " DROP TABLE
# the nthe SQL statements becomes 
# SELECT creature, count, cost FROM zoo WHERE creature="" DROP TABLE

if __name__ == '__main__':
    custom_readDB()