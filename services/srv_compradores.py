from init import mysql
from contextlib import closing



def create_comprador(user_id):
    try:
        conect = mysql.connect()
        with closing(conect.cursor()) as cursor:
            
            cursor.execute('INSERT INTO tbl_compradores(comprador_usuario) VALUES(%s)', (user_id,))

            conect.commit()
            resp = ('ok', cursor.lastrowid)
            return resp
    except Exception as ex:
        return ('error', repr(ex))
