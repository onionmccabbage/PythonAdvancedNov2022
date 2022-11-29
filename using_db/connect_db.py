import sqlite3 # this database engine is built in to python

# we need to make a connection to our database engine
# here we use 'Zoo' animals: name, count and cost
def accessDB():
    '''This function will access our Zoo database'''
    conn = sqlite3.connect('my_db') # connect or create this database
    # we need a cursor to interact with the database
    curs = conn.cursor() # this lets us execute SQL etc.
    # next we define the structure of a database table
    st = '''
    CREATE TABLE zoo 
    (
        creature VARCHAR(32) PRIMARY KEY,
        count INT,
        cost FLOAT
    )
    '''
    try: # always a good idea to put SQL execution within try block
        curs.execute(st)
        conn.commit() # this is the moment the changes are commited to the DB
        conn.close()  # tidy up - we no longer need the connection
    except Exception as err:
        print(err)

if __name__ == '__main__':
    accessDB()

# some other DB conn mechanisms
# see https://wiki.python.org/moin/DatabaseInterfaces
# DB2
# import DB2 # remember to pip isntasll first!!
# conn = DB2.connect(dsn='ibm-DB', uid='analyst', pwd='db2pwd')

# Sybase
# import Sybase
# conn = Sybase.connect('SYBASE', 'username', 'passwd', 'databasename')

# Oracle
# import cx_Oracle
# conn = cx_Oracle.connect('username', 'passwd', 'hostname:port/SID')
# conn2 = cx_Oracle.connect('username/passwd@hostname:portno/SID')
# dsn_tns = cx_Oracle.makedsn('hostname', portno, 'SID')
# conn3 = cx_Oracle.connect('username', 'passwd', dsn_tns)

# MySQL
# import MySQLdb
# conn = MySQLdb.connect(host = "hostname", user = "username",
# passwd = "password", db = "dbname")

# PySQLite
# from pysqlite2 import dbapi2 as sqlite
# conn = sqlite.connect("mydb", connectionproperties)

# ODBC
# import odbc
# conn = odbc. odbc("myDSN/username/password")