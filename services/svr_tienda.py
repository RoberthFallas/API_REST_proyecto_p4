from pymysql import connect
from pymysql.cursors import Cursor
from init import mysql
from contextlib import closing

def get_t():
    try:
        conect = mysql.connect()
        with closing(conect.cursor()) as cursor:
            cursor.execute('SELECT t.tienda_id,t.tienda_descripcion,u.usuario_nom_usr,d.direcciion_pais,d.direccion_provincia,d.direccion_canton,u.usuario_foto FROM tbl_tiendas t INNER JOIN tbl_usuarios u on t.tienda_usuario=u.usuario_id INNER JOIN tbl_direcciones d on d.direccion_id=t.tienda_direccion')
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
                cursor.execute('SELECT p.producto_id, p.producto_precio ,f.foto_url,p.producto_nombre, p.producto_descripcion, p.producto_cantidad, p.producto_publicacion, p.producto_prom_envio, p.producto_cost_env, p.producto_oferta, d.direcciion_pais, d.direccion_provincia, d.direccion_canton FROM tbl_productos p JOIN tbl_fotos f ON f.foto_id = (SELECT ff.foto_id FROM tbl_fotos ff WHERE ff.foto_producto = p.producto_id LIMIT 1) INNER JOIN tbl_direcciones d ON d.direccion_id = p.producto_direccion INNER JOIN tbl_tiendas t on t.tienda_id=p.producto_tienda where t.tienda_id=%s',(id))
            elif nombre!=None and id_categoria==None:
                 cursor.execute("SELECT p.producto_id, p.producto_precio ,f.foto_url,p.producto_nombre, p.producto_descripcion, p.producto_cantidad, p.producto_publicacion, p.producto_prom_envio, p.producto_cost_env, p.producto_oferta, d.direcciion_pais, d.direccion_provincia, d.direccion_canton FROM tbl_productos p INNER JOIN tbl_fotos f ON f.foto_id = (SELECT ff.foto_id FROM tbl_fotos ff WHERE ff.foto_producto = p.producto_id LIMIT 1)  INNER JOIN  tbl_direcciones  d ON d.direccion_id = p.producto_direccion   INNER JOIN tbl_tiendas t on t.tienda_id=p.producto_tienda where t.tienda_id=%s and p.producto_nombre like %s",(id,"%"+nombre+"%"))
            elif nombre==None and id_categoria !=None:
                 cursor.execute("SELECT p.producto_id, p.producto_precio ,f.foto_url,p.producto_nombre, p.producto_descripcion, p.producto_cantidad, p.producto_publicacion, p.producto_prom_envio, p.producto_cost_env, p.producto_oferta, d.direcciion_pais, d.direccion_provincia, d.direccion_canton FROM tbl_productos p INNER JOIN tbl_fotos f ON f.foto_id = (SELECT ff.foto_id FROM tbl_fotos ff WHERE ff.foto_producto = p.producto_id LIMIT 1) INNER JOIN  tbl_direcciones  d ON d.direccion_id = p.producto_direccion INNER JOIN tbl_tiendas t on t.tienda_id=p.producto_tienda INNER JOIN tbl_categorias c on c.categoria_id=p.producto_categoria where t.tienda_id=%s and c.categoria_id=%s",(id,id_categoria))
            else:
                 cursor.execute("SELECT p.producto_id, p.producto_precio ,f.foto_url,p.producto_nombre, p.producto_descripcion, p.producto_cantidad, p.producto_publicacion, p.producto_prom_envio, p.producto_cost_env, p.producto_oferta, d.direcciion_pais, d.direccion_provincia, d.direccion_canton FROM tbl_productos p INNER JOIN tbl_fotos f ON f.foto_id = (SELECT ff.foto_id FROM tbl_fotos ff WHERE ff.foto_producto = p.producto_id LIMIT 1) INNER JOIN  tbl_direcciones  d ON d.direccion_id = p.producto_direccion INNER JOIN tbl_tiendas t on t.tienda_id=p.producto_tienda INNER JOIN tbl_categorias c on c.categoria_id=p.producto_categoria where t.tienda_id=%s and p.producto_nombre like %s and c.categoria_id=%s",(id,"%"+nombre+"%",id_categoria))
            result=cursor.fetchall()

            return (result)
    except  Exception as ex:
        return ('error',repr(ex))

def get_fotosProductos(id):
    try:
        conect = mysql.connect()
        with  closing(conect.cursor()) as cursor:
            cursor.execute('SELECT f.foto_id,f.foto_url from tbl_fotos f where f.foto_producto= %s', (id))
            result=cursor.fetchall()
            return (result)
    except Exception as ex:
        return ('error', repr(ex))



def get_productoSelecionado(id):
    try:
        conect=mysql.connect()
        with closing(conect.cursor()) as cursor:
            cursor.execute('SELECT p.producto_id, p.producto_precio,p.producto_nombre, p.producto_descripcion, p.producto_cantidad, p.producto_publicacion, p.producto_prom_envio, p.producto_cost_env, p.producto_oferta, d.direcciion_pais, d.direccion_provincia, d.direccion_canton FROM tbl_productos p INNER JOIN tbl_direcciones d ON d.direccion_id = p.producto_direccion INNER JOIN tbl_categorias c on c.categoria_id=p.producto_categoria where p.producto_id=%s',(id))
            result=cursor.fetchall()
            return (result)
    except Exception as ex:
        return ('error',repr(ex))


def get_tienda_data_by_user_id(id):
    try:
        with closing(mysql.connect().cursor()) as cursor:
            count = cursor.execute('SELECT u.usuario_id, u.usuario_nom_usr, u.usuario_email, u.usuario_foto,'
                'u.usuario_telefono, u.usuario_cedula, u.usuario_nombre_compl, u.usuario_tipo, t.tienda_id,'
                't.tienda_descripcion, d.direccion_id, d.direcciion_pais, d.direccion_provincia, d.direccion_canton '
                'FROM tbl_tiendas t '
                'INNER JOIN tbl_usuarios u ON u.usuario_id = t.tienda_usuario '
                'INNER JOIN tbl_direcciones d ON d.direccion_id = t.tienda_direccion '
                'WHERE u.usuario_id = %s', (id,))
            if count is 1:
                    row = cursor.fetchone()
                    resp = ('ok', row)
                    return resp
            elif count is 0:
                return ('warn', 'Sin coinsidencias para el parámetro de busqueda')
            else:
                return ('error', 'Se ha cancelado la busqueda debido a que los resultados obtenidos contenian errores')
    except Exception as ex:
        return ('error',repr(ex))


def update_tienda(datos):
    try:
        conect = mysql.connect()
        with closing(conect.cursor()) as cursor:
            cursor.execute('UPDATE tbl_tiendas SET tienda_descripcion = %s WHERE tienda_id = %s', datos)
            conect.commit()
            resp = ('ok', '')
            return resp
    except Exception as ex:
        return ('error', repr(ex))

def get_subscripciones_by_id(id):
    try:
        conect=mysql.connect()
        with closing(conect.cursor()) as cursor:
            cursor.execute('SELECT c.comprador_id , u.usuario_nom_usr, u.usuario_foto FROM tbl_subscripciones t JOIN tbl_compradores c ON c.comprador_id = t.subsc_cliente JOIN tbl_usuarios u ON c.comprador_usuario = u.usuario_id WHERE t.subsc_tienda =%s',(id))
            result=cursor.fetchall()
            return ('ok',result)
    except Exception as ex:
        return ('error',repr(ex))

def get_ventas_between(startDate, endDate, id):

    try:
        conect=mysql.connect()
        with closing(conect.cursor()) as cursor:
            cursor.execute('SELECT P.producto_nombre,  ct.categoria_nombre, p.producto_precio, p.producto_oferta, p.producto_publicacion, SUM(detalle_cantidad), SUM(d.detalle_precio_final * d.detalle_cantidad) FROM `tbl_detalle` d JOIN tbl_facturas f ON d.detalle_factura = f.factura_id JOIN tbl_productos p ON p.producto_id = d.detalle_producto JOIN tbl_categorias ct ON ct.categoria_id = p.producto_categoria JOIN tbl_tiendas  t ON T.tienda_id = P.producto_tienda WHERE F.facura_fecha_hora BETWEEN %s AND %s and  t.tienda_id = %s GROUP BY detalle_producto ORDER BY SUM(detalle_cantidad) DESC ',(startDate, endDate, id))
            result=cursor.fetchall()
            return ('ok',result)
    except Exception as ex:
        return ('error',repr(ex))

def get_informacion_tienda(idTienda):
    try:
        conect=mysql.connect()
        with closing(conect.cursor()) as cursor:
            cursor.execute('SELECT u.usuario_nombre_compl,u.usuario_telefono,u.usuario_email,t.tienda_descripcion,d.direcciion_pais,d.direccion_provincia,d.direccion_canton from tbl_tiendas t inner JOIN tbl_usuarios u on u.usuario_id=t.tienda_id INNER JOIN tbl_direcciones d on d.direccion_id=t.tienda_direccion where t.tienda_id=%s',(idTienda))
            result=cursor.fetchone()
            return ('ok',result)
    except Exception as ex:
        return ('error',repr(ex))  
    