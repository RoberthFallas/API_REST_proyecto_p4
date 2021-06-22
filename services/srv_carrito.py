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

def agregar_carrito(json_data):
   try:
        conect = mysql.connect()
        query = "INSERT INTO  carrito(comprador_id,producto_id,cant) VALUES (%s,%s,%s)"
        _idCliente= json_data['idComprador']
        _idProducto = json_data['idProducto']
        _cantidad=json_data['cantidad']

        data = (_idCliente,_idProducto,_cantidad)
        with closing(conect.cursor()) as cursor:
            cursor.execute(query, data)
            conect.commit()
            id_insert =  cursor.lastrowid 
            resp=('ok', id_insert)
        return resp
   except  Exception as ex:
        return ('error', repr(ex))

def eliminar_carrito(idComprador,idProducto):
    try:
        conect = mysql.connect()
        with  closing(conect.cursor()) as cursor:
            cursor.execute('DELETE FROM carrito where carrito.comprador_id=%s and carrito.producto_id=%s', (idComprador,idProducto))
            conect.commit()
            res=jsonify('Producto eliminado del carrito')
            return res
    except Exception as ex:
        return ('error', repr(ex))