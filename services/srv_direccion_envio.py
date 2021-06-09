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
