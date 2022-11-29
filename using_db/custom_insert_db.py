# ask the user for values to enter new creatures into our DB
# (we will not validate if the creature already exists)
import sqlite3

def customInsertDB():
    '''enter sanitized user values into the DB'''
    invalid_name = True
    invalid_count = True
    invalid_cost = True
    while invalid_name:
        creature_name = input('Creature name? ')
        if type(creature_name)==str and len(creature_name)>0:
            invalid_name = False
    while invalid_count:
        count = int(float(input('How many? ')))
        if type(count)==int and count>=0:
            invalid_count = False
    while invalid_cost:
        cost = float(input('cost? '))
        if type(cost)==float and cost>=0:
            invalid_cost = False
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    st = '''
        INSERT INTO zoo
        VALUES (?, ?, ?)
    '''
    # here is the same code for populating the DB as we used before
    try:
        # we should check the values being inserted (sanitize)
        if type(creature_name)==str and creature_name != '':
            n = creature_name
        else:
            raise Exception('Name must be a non-empty string')
        if (type(count)==int and count >= 0):
            c = count
        else:
            raise Exception('count must be a positive integer')
        if (type(cost)==float and cost >= 0):
            co = cost
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
    customInsertDB()