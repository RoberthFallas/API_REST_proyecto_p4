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