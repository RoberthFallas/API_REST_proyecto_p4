from init import mysql
from contextlib import closing


def create_direccion_envio(datos):
    try:
        conect = mysql.connect()
        with closing(conect.cursor()) as cursor:
            
            cursor.execute('INSERT INTO tbl_direccion_envio(comprador_id, direccion_id, envio_cod_postal, envio_casillero, envio_observaciones) VALUES(%s, %s, %s, %s, %s)', datos)

            conect.commit()
            resp = ('ok', cursor.lastrowid)
            return resp
    except Exception as ex:
        return ('error', repr(ex))


def get_full_direccion_by_user_id(id):
    with closing(mysql.connect().cursor()) as cursor:
        try:
            cursor.execute('SELECT dir.envio_id, d.direcciion_pais, d.direccion_provincia, d.direccion_canton, '
                'dir.direccion_id, dir.envio_cod_postal, dir.envio_casillero '
                'FROM tbl_direccion_envio dir '
                'INNER JOIN tbl_direcciones d ON d.direccion_id = dir.direccion_id '
                'INNER JOIN tbl_compradores c ON c.comprador_id = dir.comprador_id '
                'WHERE c.comprador_usuario = %s and dir.envio_activa LIKE "V"', (id,))
            rows = cursor.fetchall()
            resp = ('ok', rows)
            return resp
        except Exception as ex:
            return ('error', repr(ex))


def hide_direccion_envio(id):
    try:
        conect = mysql.connect()
        with closing(conect.cursor()) as cursor:
            cursor.execute('UPDATE tbl_direccion_envio SET envio_activa = "F" WHERE envio_id = %s', (id,))
            conect.commit()
            resp = ('ok', '')
            return resp
    except Exception as ex:
        return ('error', repr(ex))
