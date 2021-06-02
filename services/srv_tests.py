from init import mysql
from contextlib import closing
from werkzeug.security import generate_password_hash
#from werkzeug.security import check_password_hash -----> si se necesita comprobar contrasenna


def test_database_conection():
    try:
        with closing(mysql.connect().cursor()) as cursor:
            cursor.execute('SELECT version()')
            result = cursor.fetchone()
            return 'Database connection: OK ------ Version: ' + result[0]
    except Exception as ex:
        casuse = repr(ex)
        return 'Database connection: FAILED-> ' + casuse


def test_pasword_encript(passw):
    try:
        conect = mysql.connect()
        with closing(conect.cursor()) as cursor:
            encrypted = generate_password_hash(passw)
            cursor.execute('INSERT INTO prueba_contrasena(contrasena) VALUES (%s)', (encrypted,))
            conect.commit()
            resp = ('ok', '')
            return resp
    except Exception as ex:
        return ('error', repr(ex))