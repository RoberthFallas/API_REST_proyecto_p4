from flask.json import jsonify
from pymysql.cursors import Cursor
from init import mysql
from contextlib import closing
import  datetime

 
 
def get_formaPagoCliente(idComprador):
    try:
        conect = mysql.connect()
        with  closing(conect.cursor()) as cursor:
            cursor.execute('SELECT fp.pago_id, fp.pago_numero_tarjeta FROM tbl_formas_pago fp WHERE fp.pago_comprador=%s',(idComprador))
            result=cursor.fetchall()
            return (result)
    except Exception as ex:
        return ('error', repr(ex))

def get_DirrecionEnvio(idComprador):
    try:
        conect = mysql.connect()
        with  closing(conect.cursor()) as cursor:
            cursor.execute('SELECT en.envio_id, d.direcciion_pais,d.direccion_provincia,d.direccion_canton,en.envio_casillero FROM tbl_direccion_envio en inner JOIN tbl_direcciones d on d.direccion_id=en.direccion_id WHERE en.comprador_id=%s',(idComprador))
            result=cursor.fetchall()
            return (result)
    except Exception as ex:
        return ('error', repr(ex))

def getCantidadProducto(idComprador):
    try:
        conect = mysql.connect()
        with  closing(conect.cursor()) as cursor:
            cursor.execute('SELECT ca.carrito_cant,p.producto_cantidad,p.producto_precio,p.producto_oferta,p.producto_cost_env from tbl_carritos ca INNER JOIN tbl_compradores c on c.comprador_id=ca.comprador_id inner JOIN tbl_productos p on p.producto_id=ca.producto_id WHERE c.comprador_id=%s',(idComprador))
            result=cursor.fetchall()
            return (result)
    except Exception as ex:
        return ('error', repr(ex))

def getFormaPagoSeleccionada(idComprador,idFormaPago):
    try:
        conect = mysql.connect()
        with  closing(conect.cursor()) as cursor:
            cursor.execute('SELECT fg.pago_saldo FROM tbl_formas_pago fg inner JOIN tbl_compradores c on fg.pago_comprador=c.comprador_id WHERE c.comprador_id=%s and fg.pago_id=%s',(idComprador,idFormaPago))
            return ('ok', cursor.fetchone())   
    except Exception as ex:
        return ('error', repr(ex))

def insertarFactura(idComprador,idFormaPago,subtotal,factura_total):
    try:
        fecha=datetime.datetime.now()
        conect = mysql.connect()
        query = "INSERT INTO tbl_facturas (factura_comprador,factura_metodo_pago,facura_fecha_hora,factura_subtotal,factura_total) VALUES (%s,%s,%s,%s,%s)"

        data = (idComprador,idFormaPago,fecha,subtotal,factura_total)
        with closing(conect.cursor()) as cursor:
            cursor.execute(query, data)
            conect.commit()
            id_insert =  cursor.lastrowid 
            resp=('ok', id_insert)
        return resp
    except  Exception as ex:
        return ('error', repr(ex))