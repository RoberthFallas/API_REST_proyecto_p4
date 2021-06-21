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


def get_comprador_id_by_user_id(id):
    with closing(mysql.connect().cursor()) as cursor:
        try:
            cursor.execute('SELECT c.comprador_id FROM tbl_compradores c '
            'WHERE c.comprador_usuario = %s', (id,))
            rows = cursor.fetchone()
            resp = ('ok', rows[0])
            return resp
        except Exception as ex:
            return ('error', repr(ex))
