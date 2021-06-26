from flask.json import jsonify
from pymysql.cursors import Cursor
from init import mysql
from contextlib import closing


def insertar_reporte(json_data):
    try:
        conect = mysql.connect()
        query = "INSERT INTO tbl_denuncias(comprador_id,tienda_id,denuncia_estado,denuncia_descripcion) VALUES (%s,%s,%s,%s)"
        _idComprador= json_data['idComprador']
        _idProducto = json_data['idTienda']
        _estado= json_data['estado']
        _descripcion = json_data['descripcion']

        data = (_idComprador, _idProducto,_estado,_descripcion)

        with closing(conect.cursor()) as cursor:

            cursor.execute(query,data)
            conect.commit()
            id_insert =  cursor.lastrowid 
            resp=('ok', id_insert)
            return resp
    except  Exception as ex:
        return ('error', repr(ex))

def get_comprasReporte(idComprador,idTienda):
    try:
        conect = mysql.connect()
        with  closing(conect.cursor()) as cursor:
            cursor.execute('SELECT count(fa.factura_id) FROM tbl_facturas fa inner JOIN tbl_detalle d on d.detalle_factura=fa.factura_id INNER join tbl_productos p on p.producto_id=d.detalle_producto INNER JOIN tbl_tiendas t on t.tienda_id=p.producto_id WHERE fa.factura_comprador=%s and t.tienda_id=%s',(idComprador,idTienda))
            result=cursor.fetchone()
            return ('ok',result)
    except Exception as ex:
        return ('error', repr(ex))

def get_reportesRealizados(idComprador,idTienda):
    try:
        conect = mysql.connect()
        with  closing(conect.cursor()) as cursor:
            cursor.execute('SELECT COUNT(d.comprador_id) from tbl_denuncias d WHERE d.comprador_id=%s AND d.tienda_id=%s',(idComprador,idTienda))
            result=cursor.fetchone()
            return ('ok',result)
    except Exception as ex:
        return ('error', repr(ex))

def eliminar_reporte(idComprador,idTienda):
    try:
        conect = mysql.connect()
        with  closing(conect.cursor()) as cursor:
            cursor.execute('DELETE FROM tbl_denuncias where tbl_denuncias.comprador_id=%s and tbl_denuncias.tienda_id=%s', (idComprador,idTienda))
            conect.commit()
            res=jsonify('Reporte eliminado correctamente')
            return res
    except Exception as ex:
        return ('error', repr(ex))


def get_denuncias_by_tienda(id):
    try:
        conect = mysql.connect()
        with  closing(conect.cursor()) as cursor:
            cursor.execute('SELECT COUNT(d.comprador_id) FROM tbl_denuncias d WHERE d.tienda_id = %s',(id)) 
            result=cursor.fetchone()
            print(result)
            return ('ok', result)
    except Exception as ex:
        return ('error', repr(ex))