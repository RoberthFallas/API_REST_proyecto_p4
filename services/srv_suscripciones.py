from flask.json import jsonify
from pymysql.cursors import Cursor
from init import mysql
from contextlib import closing

'INSERT INTO tbl_subscripciones(tbl_subscripciones.subsc_cliente,tbl_subscripciones.subsc_tienda)VALUES(1,1)'
 
 
def get_suscripcion(idComprador,idTienda):
    try:
        conect = mysql.connect()
        with  closing(conect.cursor()) as cursor:
            cursor.execute('SELECT sub.subsc_cliente,sub.subsc_tienda FROM tbl_subscripciones sub WHERE sub.subsc_cliente=%s and sub.subsc_tienda=%s',(idComprador,idTienda))
            result=cursor.fetchall()
            return (result)
    except Exception as ex:
        return ('error', repr(ex))

def eliminar_suscripcion(idComprador,idTienda):
    try:
        conect = mysql.connect()
        with  closing(conect.cursor()) as cursor:
            cursor.execute('DELETE FROM tbl_subscripciones where tbl_subscripciones.subsc_cliente=%s and tbl_subscripciones.subsc_tienda=%s', (idComprador,idTienda))
            conect.commit()
            res=jsonify('Comentario eliminado correctamente')
            return res
    except Exception as ex:
        return ('error', repr(ex))

def insertar_suscripcion(json_data):
    try:
        conect = mysql.connect()
        query = "INSERT INTO tbl_subscripciones(subsc_cliente,subsc_tienda) VALUES (%s,%s)"
        _idCliente= json_data['idComprador']
        _idTienda = json_data['idTienda']

        data = (_idCliente,_idTienda)

        with closing(conect.cursor()) as cursor:

            cursor.execute(query, data)
            conect.commit()
            id_insert =  cursor.lastrowid 
            resp=('ok', id_insert)
            return resp
    except  Exception as ex:
        return ('error', repr(ex))

def get_miSuscripcion(idComprador):
    try:
        conect = mysql.connect()
        with  closing(conect.cursor()) as cursor:
            cursor.execute('SELECT t.tienda_id,u.usuario_nombre_compl,u.usuario_foto FROM tbl_compradores c inner JOIN tbl_subscripciones s on s.subsc_cliente=c.comprador_id INNER JOIN tbl_tiendas t on t.tienda_id=s.subsc_tienda inner JOIN tbl_usuarios u on u.usuario_id=t.tienda_id where c.comprador_id=%s',(idComprador))
            result=cursor.fetchall()
            return (result)
    except Exception as ex:
        return ('error', repr(ex))