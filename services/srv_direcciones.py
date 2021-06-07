from init import mysql
from contextlib import closing


def create_direccion(datos):
    try:
        conect = mysql.connect()
        with closing(conect.cursor()) as cursor:
            cursor.execute('INSERT INTO tbl_direcciones(direcciion_pais, direccion_provincia, direccion_canton) VALUES(%s, %s, %s)', datos)
            conect.commit()
            resp = ('ok', cursor.lastrowid)
            return resp
    except Exception as ex:
        return ('error', repr(ex))