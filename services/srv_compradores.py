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


def get_comprador(id):
    try:
        conect = mysql.connect()
        with closing(conect.cursor()) as cursor:
            
            cursor.execute('SELECT u.usuario_nom_usr, u.usuario_email, u.usuario_foto, u.usuario_telefono, u.usuario_nombre_compl FROM tbl_usuarios u JOIN tbl_compradores c ON c.comprador_usuario = usuario_id WHERE c.comprador_id = %s', (id,))

            resp = ('ok', cursor.fetchone())
            return resp
    except Exception as ex:
        return ('error', repr(ex))