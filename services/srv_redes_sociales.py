from init import mysql
from contextlib import closing



def get_redes_sociales(id):
    try:
        conect = mysql.connect()
        with closing(conect.cursor()) as cursor:
            
            cursor.execute('SELECT r.red_id, r.red_nombre, r.red_direccion '
                            'FROM tbl_redes_sociales r '
                            'WHERE r.red_usuario = %s', (id,))
            data = cursor.fetchall()
            resp = ('ok', data)
            return resp
    except Exception as ex:
        return ('error', repr(ex))



def create_red_social(list_data):
    try:
        conect = mysql.connect()
        with closing(conect.cursor()) as cursor:
            cursor.execute('INSERT INTO tbl_redes_sociales(red_usuario, red_nombre, red_direccion) '
            'VALUES(%s, %s, %s)', list_data)
            conect.commit()
            resp = ('ok', '')
            return resp
    except Exception as ex:
        return ('error', repr(ex))



def update_red_social(red_id, direccion):
    try:
        conect = mysql.connect()
        with closing(conect.cursor()) as cursor:
            cursor.execute('UPDATE tbl_redes_sociales '
                'SET red_direccion = %s WHERE red_id = %s', (direccion, red_id,))
            conect.commit()
            resp = ('ok', '')
            return resp
    except Exception as ex:
        return ('error', repr(ex))