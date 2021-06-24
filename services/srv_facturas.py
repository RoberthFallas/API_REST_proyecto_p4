from pymysql.cursors import Cursor
from init import mysql
from contextlib import closing


def get_factura_by_id(id):
    try:
        conect = mysql.connect()
        with  closing(conect.cursor()) as cursor:
            cursor.execute('SELECT  u.usuario_nombre_compl, u.usuario_cedula, u.usuario_email, u.usuario_telefono, dr.direcciion_pais, dr.direccion_provincia, dr.direccion_canton, den.envio_cod_postal, den.envio_casillero, den.envio_observaciones, fp.pago_numero_tarjeta, gr.giro_resultado, f.factura_subtotal, f.factura_total FROM tbl_facturas f JOIN tbl_compradores c ON c.comprador_id = f.factura_comprador JOIN tbl_usuarios u ON u.usuario_id = c.comprador_usuario JOIN tbl_direccion_envio den ON den.envio_id = f.envio_id JOIN tbl_direcciones dr ON den.direccion_id = dr.direccion_id JOIN tbl_formas_pago fp ON fp.pago_id = f.factura_metodo_pago LEFT JOIN tbl_giros_ruleta gr ON gr.giro_id = f.factura_regalia WHERE f.factura_id =  %s',(id))
            result=cursor.fetchone()
            return ('ok',result)
    except Exception as ex:
        return ('error', repr(ex))

def get_factura_detalles_by_id(id):
    try:
        conect = mysql.connect()
        with  closing(conect.cursor()) as cursor:
            cursor.execute('SELECT  p.producto_nombre,SUM(detalle_cantidad), d.detalle_precio_final, SUM(d.detalle_precio_final * d.detalle_cantidad), u.usuario_nombre_compl, p.producto_cost_env FROM tbl_facturas f JOIN tbl_detalle d ON d.detalle_factura = f.factura_id JOIN tbl_productos p ON p.producto_id = d.detalle_producto JOIN tbl_tiendas t ON t.tienda_id = p.producto_tienda JOIN tbl_usuarios u ON u.usuario_id  = t.tienda_usuario WHERE f.factura_id =  %s GROUP BY d.detalle_precio_final,d.detalle_producto',(id))
            result=cursor.fetchall()
            return ('ok' , result)
    except Exception as ex:
        return ('error', repr(ex))