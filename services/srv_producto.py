from pymysql.cursors import Cursor
from init import mysql
from contextlib import closing
from werkzeug.security import generate_password_hash, check_password_hash

def create_product(data_json, dir):
 try:
        conect = mysql.connect()

        query = "INSERT INTO tbl_productos( producto_direccion, producto_categoria, producto_tienda, producto_nombre, producto_descripcion, producto_precio, producto_cantidad, producto_publicacion, producto_prom_envio, producto_cost_env) VALUES (%s,%s,%s,%s,%s,%s,%s,CURRENT_DATE(),%s,%s)"
        _direccion = dir
        _categoria = data_json['categoria']
        _tienda = data_json['id']
        _nombre = data_json['nombre']
        _descripcion = data_json['descripcion']
        _precio = data_json['precio']
        _cantidad = data_json['cantidad']
        _duracion = data_json['duracion']
        _costo = data_json['costo']

        data = (_direccion, _categoria,  _tienda, _nombre,_descripcion, _precio, _cantidad,_duracion, _costo)

        with closing(conect.cursor()) as cursor:

            cursor.execute(query, data)
            conect.commit()

            
            id_insert =  cursor.lastrowid 

            return ('ok', id_insert)

           
 except Exception as ex:
        return ('error', repr(ex))


