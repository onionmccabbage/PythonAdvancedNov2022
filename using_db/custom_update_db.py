# ask the user for values to be used in updating members of our database
import sqlite3

def custom_update_db():
    '''Take parameters for name, count and cost then update that data member'''
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    invalid = True
    while invalid:
        which_creature = input('Which creature need updating? ')
        if (type(which_creature)==str and which_creature !=''):
            invalid=False
    # ask for the new quantity
    qty = int(float(input('What is the updated quantity? ')))
    st = '''
    UPDATE zoo
    SET count = {0}
    WHERE creature IS "{1}"
    '''.format(qty, which_creature)
    try:
        curs.execute(st)
        conn.commit()
    except Exception as err:
        print(err)
    finally:
        conn.close()


if __name__ == '__main__':
    custom_update_db()