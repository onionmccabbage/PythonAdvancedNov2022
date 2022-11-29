import sqlite3

def writeDB():
    '''write a single creature to our Zoo table'''
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    st = '''
    INSERT INTO zoo
    VALUES ("Penguin", 256, 0.62)
    '''
    try:
        curs.execute(st)
        conn.commit()
    except Exception as err:
        print(err)
    finally:
        conn.close()

if __name__ == '__main__':
    writeDB()