from flask.json import jsonify
from pymysql.cursors import Cursor
from init import mysql
from contextlib import closing


 
 
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