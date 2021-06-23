from flask.json import jsonify
from pymysql.cursors import Cursor
from init import mysql
from contextlib import closing

def get_deseo(idComprador,idProducto):
    try:
        conect = mysql.connect()
        with  closing(conect.cursor()) as cursor:
            cursor.execute('SELECT d.deseo_comprador,d.deseo_producto from tbl_deseos d WHERE d.deseo_comprador=%s and d.deseo_producto=%s',(idComprador,idProducto))
            result=cursor.fetchall()
            return (result)
    except Exception as ex:
        return ('error', repr(ex))

def eliminar_deseo(idComprador,idProducto):
    try:
        conect = mysql.connect()
        with  closing(conect.cursor()) as cursor:
            cursor.execute('DELETE FROM tbl_deseos where tbl_deseos.deseo_comprador=%s and tbl_deseos.deseo_producto=%s', (idComprador,idProducto))
            conect.commit()
            res=jsonify('deseo eliminado correctamente')
            return res
    except Exception as ex:
        return ('error', repr(ex))

def insertar_deseo(json_data):
    try:
        conect = mysql.connect()
        query = "INSERT INTO tbl_deseos(deseo_comprador,deseo_producto) VALUES (%s,%s)"
        _idCliente= json_data['idComprador']
        _idProducto = json_data['idProducto']

        data = (_idCliente,_idProducto)

        with closing(conect.cursor()) as cursor:

            cursor.execute(query, data)
            conect.commit()
            id_insert =  cursor.lastrowid 
            resp=('ok', id_insert)
            return resp
    except  Exception as ex:
        return ('error', repr(ex))


def get_misDeseos(idComprador):
    try:
        conect = mysql.connect()
        with  closing(conect.cursor()) as cursor:
            cursor.execute('SELECT p.producto_id,p.producto_nombre,p.producto_descripcion,f.foto_url FROM tbl_deseos t INNER JOIN tbl_productos p on t.deseo_producto=p.producto_id inner JOIN tbl_fotos f ON f.foto_id=(SELECT ff.foto_id FROM tbl_fotos ff WHERE ff.foto_producto=p.producto_id LIMIT 1) WHERE t.deseo_comprador=%s',(idComprador))
            result=cursor.fetchall()
            return (result)
    except Exception as ex:
        return ('error', repr(ex))