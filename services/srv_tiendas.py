from init import mysql
from contextlib import closing



def create_tienda(datos):
    try:
        conect = mysql.connect()
        with closing(conect.cursor()) as cursor:
            
            cursor.execute('INSERT INTO tbl_tiendas(tienda_usuario, tienda_direccion, tienda_descripcion) VALUES(%s, %s, %s)', datos)

            conect.commit()
            resp = ('ok', cursor.lastrowid)
            return resp
    except Exception as ex:
        return ('error', repr(ex))