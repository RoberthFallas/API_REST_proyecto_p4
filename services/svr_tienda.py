from pymysql.cursors import Cursor
from init import mysql
from contextlib import closing

def get_t():
    try:
        conect = mysql.connect()
        with closing(conect.cursor()) as cursor:
            cursor.execute('SELECT t.tienda_id,t.tienda_descripcion,u.usuario_nom_usr,d.direcciion_pais,d.direccion_provincia,d.direccion_canton FROM tbl_tiendas t INNER JOIN tbl_usuarios u on t.tienda_usuario=u.usuario_id INNER JOIN tbl_direcciones d on d.direccion_id=t.tienda_direccion')
            result = cursor.fetchall()
            return (result)
    except Exception as ex:
        return ('error', repr(ex))

def get_categorias(id):
    try:
        conect = mysql.connect()
        with  closing(conect.cursor()) as cursor:
            cursor.execute('SELECT c.categoria_nombre from tbl_tiendas t INNER JOIN tbl_productos p on p.producto_tienda=t.tienda_id INNER JOIN tbl_categorias c on p.producto_categoria=c.categoria_id where t.tienda_id=%s', (id))
            result=cursor.fetchall()
            return (result)
    except Exception as ex:
        return ('error', repr(ex))