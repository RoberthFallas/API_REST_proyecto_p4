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
            cursor.execute('SELECT DISTINCT c.categoria_id, c.categoria_nombre from tbl_tiendas t INNER JOIN tbl_productos p on p.producto_tienda=t.tienda_id INNER JOIN tbl_categorias c on p.producto_categoria=c.categoria_id where t.tienda_id=%s', (id))
            result=cursor.fetchall()
            return (result)
    except Exception as ex:
        return ('error', repr(ex))

def get_productosTiendas(id,nombre=None,id_categoria=None):
    try:
        conect = mysql.connect()
        with closing(conect.cursor()) as cursor:
           # if nombre==None:
           #    cursor.execute('SELECT p.producto_id, p.producto_precio ,f.foto_url,p.producto_nombre FROM tbl_productos p INNER JOIN tbl_fotos f on p.producto_id=f.foto_id INNER JOIN tbl_tiendas t on t.tienda_id=p.producto_tienda where t.tienda_id=%s',(id))
           #else:
           #     cursor.execute("SELECT p.producto_id, p.producto_precio ,f.foto_url,p.producto_nombre FROM tbl_productos p INNER JOIN tbl_fotos f on p.producto_id=f.foto_id INNER JOIN tbl_tiendas t on t.tienda_id=p.producto_tienda where t.tienda_id=%s and p.producto_nombre like %s",(id,"%"+nombre+"%"))
            if nombre==None and id_categoria==None:
                cursor.execute('SELECT p.producto_id, p.producto_precio ,f.foto_url,p.producto_nombre FROM tbl_productos p INNER JOIN tbl_fotos f on p.producto_id=f.foto_id INNER JOIN tbl_tiendas t on t.tienda_id=p.producto_tienda where t.tienda_id=%s',(id))
            elif nombre!=None and id_categoria==None:
                 cursor.execute("SELECT p.producto_id, p.producto_precio ,f.foto_url,p.producto_nombre FROM tbl_productos p INNER JOIN tbl_fotos f on p.producto_id=f.foto_id INNER JOIN tbl_tiendas t on t.tienda_id=p.producto_tienda where t.tienda_id=%s and p.producto_nombre like %s",(id,"%"+nombre+"%"))
            elif nombre==None and id_categoria !=None:
                 cursor.execute("SELECT p.producto_id, p.producto_precio ,f.foto_url,p.producto_nombre FROM tbl_productos p INNER JOIN tbl_fotos f on p.producto_id=f.foto_id INNER JOIN tbl_tiendas t on t.tienda_id=p.producto_tienda INNER JOIN tbl_categorias c on c.categoria_id=p.producto_categoria where t.tienda_id=%s and c.categoria_id=%s",(id,id_categoria))
            else:
                 cursor.execute("SELECT p.producto_id, p.producto_precio ,f.foto_url,p.producto_nombre FROM tbl_productos p INNER JOIN tbl_fotos f on p.producto_id=f.foto_id INNER JOIN tbl_tiendas t on t.tienda_id=p.producto_tienda INNER JOIN tbl_categorias c on c.categoria_id=p.producto_categoria where t.tienda_id=%s and p.producto_nombre like %s and c.categoria_id=%s",(id,"%"+nombre+"%",id_categoria))
            result=cursor.fetchall()
            return (result)
    except  Exception as ex:
        return ('error',repr(ex))