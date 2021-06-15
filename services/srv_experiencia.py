from pymysql.cursors import Cursor
from init import mysql
from contextlib import closing

def insert_calificacion_producto(json_data):
 try:
        conect = mysql.connect()

        query = "INSERT INTO tbl_evaluacion_productos (comprador_id,producto_id,evaluacion_estrellas) VALUES (%s,%s,%s)" 

        _comprador= json_data['idComprador']
        _producto = json_data['idProducto']
        _calificacion = json_data['calificacion']

        data = (_comprador, _producto,_calificacion)

        with closing(conect.cursor()) as cursor:

            cursor.execute(query, data)
            conect.commit()

            id_insert =  cursor.lastrowid 

            return ('ok', id_insert)

           
 except Exception as ex:
        return ('error', repr(ex))