from init import mysql
from contextlib import closing

def test_database_conection():
    try:
        with closing(mysql.connect().cursor()) as cursor:
            cursor.execute('SELECT version()')
            result = cursor.fetchone()
            return 'Database connection: OK ------ Version: ' + result[0]
    except Exception as ex:
        casuse = repr(ex)
        return 'Database connection: FAILED-> ' + casuse
