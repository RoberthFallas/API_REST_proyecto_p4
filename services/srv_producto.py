from pymysql.cursors import Cursor
from init import mysql
from contextlib import closing
import os

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


def delete_producto(id):
      try:
        conect = mysql.connect()
      
        with closing(conect.cursor()) as cursor:
            resp = delelete_images_server(id)
            if(resp == 'ok'):
                     query = "DELETE FROM tbl_productos WHERE tbl_productos.producto_id ="+ id
                     cursor.execute(query)
                     query = "SELECT p.producto_direccion FROM tbl_productos p WHERE p.producto_id ="+ id
                     cursor.execute(query)
                     conect.commit()
                     id_direccion = cursor.fetchone()
                     print(id_direccion)
                     query = "DELETE FROM tbl_direcciones WHERE tbl_direcciones.direccion_id ="+ id
                     cursor.execute(query)
                     conect.commit()
                     return ('ok')
              
            return "No se eliminaron las imagenes"


          
     
      except Exception as ex:
        return ('error', repr(ex))

def delelete_images_server(id):
      try:
        conect = mysql.connect()

        queryFotos = "SELECT f.foto_url FROM tbl_fotos f WHERE f.foto_producto = " + id  
        queryDeleteFotos = "DELETE FROM tbl_fotos WHERE tbl_fotos.foto_producto = " + id  


        with closing(conect.cursor()) as cursor:

            cursor.execute(queryFotos)
            fotos_nombres = cursor.fetchall()
            print(queryDeleteFotos)
            cursor.execute(queryDeleteFotos)
            conect.commit()

            for result in fotos_nombres:
                filename = result[0]
                print(filename)
                os.remove(os.getcwd() + '/resources/images/' + filename)

            return 'ok'
      except Exception as ex:
        return ('error', repr(ex))

       
     
