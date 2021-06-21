from flask.json import jsonify
from pymysql.cursors import Cursor
from init import mysql
from contextlib import closing

def get_miCarrito(idComprador):
    try:
        conect = mysql.connect()
        with  closing(conect.cursor()) as cursor:
            cursor.execute('SELECT p.producto_id,p.producto_nombre,p.producto_descripcion,f.foto_url,t.cant FROM carrito t INNER JOIN tbl_productos p on t.producto_id=p.producto_id inner JOIN tbl_fotos f ON f.foto_id=(SELECT ff.foto_id FROM tbl_fotos ff WHERE ff.foto_producto=p.producto_id LIMIT 1) WHERE t.comprador_id=%s',(idComprador))
            result=cursor.fetchall()
            return (result)
    except Exception as ex:
        return ('error', repr(ex))
