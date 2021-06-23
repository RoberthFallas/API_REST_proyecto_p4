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


def get_compras_between(id, startDate, endDate):
    try:
        conect = mysql.connect()
        with closing(conect.cursor()) as cursor:
            
            cursor.execute('SELECT  u.usuario_nom_usr, p.producto_nombre,p.producto_descripcion, ct.categoria_nombre, p.producto_precio,SUM(detalle_cantidad), SUM(d.detalle_precio_final * d.detalle_cantidad), f.factura_id, d.detalle_precio_final, fp.pago_numero_tarjeta FROM tbl_facturas f JOIN tbl_detalle d ON d.detalle_factura = f.factura_id JOIN tbl_productos p ON p.producto_id = d.detalle_producto JOIN tbl_categorias ct ON ct.categoria_id  = p.producto_categoria JOIN  tbl_formas_pago fp ON f.factura_metodo_pago = fp.pago_id  JOIN tbl_compradores cp ON cp.comprador_id = f.factura_comprador JOIN tbl_usuarios u on cp.comprador_usuario = u.usuario_id WHERE cp.comprador_id = %s  and f.facura_fecha_hora BETWEEN %s  and %s GROUP BY d.detalle_precio_final,d.detalle_producto  ORDER BY SUM(f.factura_id) ', (id, startDate, endDate))
            data = cursor.fetchall()
            resp = ('ok', data)
            return resp
    except Exception as ex:
        return ('error', repr(ex))


def get_productos_mas_dinero(id, startDate, endDate):
    try:
        conect = mysql.connect()
        with closing(conect.cursor()) as cursor:
            
            cursor.execute('SELECT   p.producto_nombre,SUM(detalle_cantidad), SUM(d.detalle_precio_final * d.detalle_cantidad) FROM tbl_facturas f JOIN tbl_detalle d ON d.detalle_factura = f.factura_id JOIN tbl_productos p ON p.producto_id = d.detalle_producto  JOIN tbl_compradores cp ON cp.comprador_id = f.factura_comprador  WHERE cp.comprador_id = %s and f.facura_fecha_hora BETWEEN %s and %s  GROUP BY d.detalle_producto  ORDER BY SUM(d.detalle_precio_final) desc LIMIT 10', (id, startDate, endDate))
            data = cursor.fetchall()
            resp = ('ok', data)
            return resp
    except Exception as ex:
        return ('error', repr(ex))

def get_subscripciones(id_comprador):
    try:
        conect = mysql.connect()
        with closing(conect.cursor()) as cursor:
            
            cursor.execute('SELECT t.tienda_id, u.usuario_nombre_compl, u.usuario_nom_usr, t.tienda_descripcion FROM tbl_subscripciones s JOIN tbl_tiendas t ON t.tienda_id = s.subsc_tienda JOIN tbl_compradores c ON c.comprador_id = s.subsc_cliente JOIN tbl_usuarios u ON t.tienda_usuario= u.usuario_id WHERE c.comprador_id = %s ', (id_comprador))
            data = cursor.fetchall()
            resp = ('ok', data)
            return resp
    except Exception as ex:
        return ('error', repr(ex))

def get_deseos_by_tienda(idComprador, idTienda):
    try:
        conect = mysql.connect()
        with closing(conect.cursor()) as cursor:
            
            cursor.execute('SELECT p.producto_nombre , p.producto_precio FROM tbl_deseos d JOIN tbl_compradores c ON  c.comprador_id = d.deseo_comprador JOIN  tbl_productos p ON p.producto_id = d.deseo_producto JOIN tbl_tiendas t ON t.tienda_id = p.producto_tienda  WHERE c.comprador_id = %s AND t.tienda_id = %s', (idComprador, idTienda))
            data = cursor.fetchall()
            resp = ('ok', data)
            return resp
    except Exception as ex:
        return ('error', repr(ex))


