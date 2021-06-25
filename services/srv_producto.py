from pymysql.cursors import Cursor
from init import mysql
from contextlib import closing
import os

def create_product(data_json, dir):
 try:
        conect = mysql.connect()

        query = "INSERT INTO tbl_productos( producto_direccion, producto_categoria, producto_tienda, producto_nombre, producto_descripcion, producto_precio, producto_cantidad, producto_publicacion, producto_prom_envio, producto_cost_env, producto_oferta) VALUES (%s,%s,%s,%s,%s,%s,%s,CURRENT_DATE(),%s,%s, %s)"
        _direccion = dir
        _categoria = data_json['categoria']
        _tienda = data_json['id']
        _nombre = data_json['nombre']
        _descripcion = data_json['descripcion']
        _precio = data_json['precio']
        _cantidad = data_json['cantidad']
        _duracion = data_json['duracion']
        _costo = data_json['costo']
        _oferta = data_json['precioOferta']

        data = (_direccion, _categoria,  _tienda, _nombre,_descripcion, _precio, _cantidad,_duracion, _costo, _oferta)

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
            print(resp)
            if(resp == 'ok'):
                     query = "DELETE FROM tbl_productos WHERE tbl_productos.producto_id ="+ id
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
              if(result[0] != None):
                  filename = result[0]
                  print(filename, " se elimino")
                  os.remove(os.getcwd() + '/resources/images/' + filename)

            return 'ok'
      except Exception as ex:
        return ('error', repr(ex))

def delete_images_update(images_delete):
  
  for image in images_delete:
    filename = image.rsplit('/', 1)[-1]
    print(filename)
    print(delete_images_by_url(filename))
 

def delete_images_by_url(filename):
     try:
        conect = mysql.connect()
       
        queryDeleteFotos = "DELETE FROM tbl_fotos WHERE tbl_fotos.foto_url = '" + filename + "'" 
        print(queryDeleteFotos)
        with closing(conect.cursor()) as cursor:

            cursor.execute(queryDeleteFotos)
            conect.commit()
            print('imagen eliminada ')
            os.remove(os.getcwd() + '/resources/images/' + filename)

            return 'ok'
     except Exception as ex:
        return ('error', repr(ex))

def update_product(data_json): #esta en desarrollo
  try:
          conect = mysql.connect()

          query = "UPDATE tbl_productos SET producto_categoria=%s,producto_nombre=%s,producto_descripcion =%s,producto_precio=%s,producto_cantidad=%s,producto_prom_envio=%s,producto_cost_env=%s,producto_oferta=%s WHERE producto_id = %s"

          _categoria = data_json['categoria']
          _nombre = data_json['nombre']
          _descripcion = data_json['descripcion']
          _precio = data_json['precio']
          _cantidad = data_json['cantidad']
          _duracion = data_json['duracion']
          _costo = data_json['costo']
          _oferta = data_json['precioOferta']
          _id_producto = data_json['idProducto']

          data = (_categoria, _nombre, _descripcion, _precio, _cantidad, _duracion, _costo, _oferta, _id_producto)

          with closing(conect.cursor()) as cursor:

              cursor.execute(query, data)
              conect.commit()
              return ('ok')

            
  except Exception as ex:
          return ('error', repr(ex))  
  


def get_product_by_id(id):
  try:
      conect = mysql.connect()
      with closing(conect.cursor()) as cursor:
   
        cursor.execute('SELECT p.producto_id, p.producto_precio ,p.producto_nombre, p.producto_descripcion, p.producto_cantidad, p.producto_publicacion, p.producto_prom_envio, p.producto_cost_env, p.producto_oferta, d.direcciion_pais, d.direccion_provincia, d.direccion_canton, p.producto_categoria, p.producto_direccion FROM tbl_productos p INNER JOIN tbl_direcciones d ON d.direccion_id = p.producto_direccion where p.producto_id=%s',(id))
      
        result=cursor.fetchall()

        return ('ok' ,result)
  except  Exception as ex:
      return ('error',repr(ex))


def get_calificacion(id):
  try:
      conect = mysql.connect()
      with closing(conect.cursor()) as cursor:

        e = []

        for x in range(0, 5):
          query = 'SELECT COUNT(p.evaluacion_estrellas) FROM  tbl_evaluacion_productos p WHERE p.evaluacion_estrellas = %s AND p.producto_id = %s'
          data = (x+1, id)
          cursor.execute(query, data)
          e.append ( cursor.fetchone()[0])
          print(e[x])
        
        try:
          calificacion = (1*e[0] + 2*e[1]  + 3*e[2] + 4*e[3] + 5*e[4]) / (e[0] + e[1] + e[2] + e[3] + e[4]) 
        except ZeroDivisionError:
          calificacion = 0

        return ('ok', calificacion)
  except  Exception as ex:
      return ('error',repr(ex))


def get_deseos(id):
  try:
        conect=mysql.connect()
        with closing(conect.cursor()) as cursor:
            cursor.execute('SELECT c.comprador_id , u.usuario_nom_usr, u.usuario_foto FROM tbl_deseos t JOIN tbl_compradores c ON c.comprador_id = t.deseo_comprador JOIN tbl_usuarios u ON c.comprador_usuario = u.usuario_id WHERE t.deseo_producto = %s',(id))
            result=cursor.fetchall()
            return ('ok',result)
  except Exception as ex:
        return ('error',repr(ex))

def get_cant_deseos(id):
  try:
        conect=mysql.connect()
        with closing(conect.cursor()) as cursor:
            cursor.execute('SELECT COUNT(t.deseo_producto) FROM tbl_deseos t WHERE t.deseo_producto = %s',(id))
            result=cursor.fetchone()
            return ('ok',result)
  except Exception as ex:
        return ('error',repr(ex))


def update_product_cantidad(idCantidad,idProducto): #esta en desarrollo
  try:
          conect = mysql.connect()

          query = "UPDATE tbl_productos SET producto_cantidad=%s WHERE producto_id = %s"

          data = (idCantidad,idProducto)

          with closing(conect.cursor()) as cursor:

              cursor.execute(query, data)
              conect.commit()
              return ('ok')

            
  except Exception as ex:
          return ('error', repr(ex))  
     
def get_productosMasVendidos():
   try:
      conect = mysql.connect()
      with closing(conect.cursor()) as cursor:
   
        cursor.execute('SELECT p.producto_id, p.producto_nombre,p.producto_descripcion,p.producto_precio,p.producto_cantidad,fo.foto_url,SUM(detalle_cantidad),p.producto_cost_env,p.producto_prom_envio,p.producto_oferta FROM tbl_detalle d JOIN tbl_facturas f ON d.detalle_factura = f.factura_id JOIN tbl_productos p ON p.producto_id = d.detalle_producto inner join tbl_fotos fo on fo.foto_producto=p.producto_id GROUP BY detalle_producto ORDER BY SUM(detalle_cantidad) DESC LIMIT 10')
        result=cursor.fetchall()

        return (result)
   except  Exception as ex:
      return ('error',repr(ex))

def get_ofertas(categoria, precio_menor, precio_mayor, fecha_inicio, fecha_final):
  try:
    conect = mysql.connect()
    with closing(conect.cursor()) as cursor:
      if categoria !=None and (precio_menor==None and precio_mayor==None) and (fecha_inicio == None and fecha_final == None) :
        cursor.execute('SELECT p.producto_publicacion, p.producto_nombre,p.producto_descripcion, p.producto_precio, p.producto_oferta, c.categoria_nombre, u.usuario_nombre_compl FROM tbl_productos p JOIN tbl_categorias c ON c.categoria_id = p.producto_categoria  JOIN tbl_tiendas t ON t.tienda_id = p.producto_tienda  JOIN tbl_usuarios u ON u.usuario_id = t.tienda_usuario WHERE  p.producto_oferta > 0 and  c.categoria_id =%s',(categoria))
      elif (precio_menor!=None and precio_mayor!=None) and categoria == None and (fecha_inicio == None and fecha_final == None)  :
        cursor.execute("SELECT p.producto_publicacion, p.producto_nombre,p.producto_descripcion, p.producto_precio, p.producto_oferta, c.categoria_nombre, u.usuario_nombre_compl FROM tbl_productos p JOIN tbl_categorias c ON c.categoria_id = p.producto_categoria  JOIN tbl_tiendas t ON t.tienda_id = p.producto_tienda  JOIN tbl_usuarios u ON u.usuario_id = t.tienda_usuario WHERE p.producto_oferta > 0 and p.producto_oferta BETWEEN %s and %s",(precio_menor, precio_mayor))
      elif (fecha_inicio != None and fecha_final != None) and (precio_menor==None and precio_mayor==None) and categoria == None :
        cursor.execute("SELECT p.producto_publicacion, p.producto_nombre,p.producto_descripcion, p.producto_precio, p.producto_oferta, c.categoria_nombre, u.usuario_nombre_compl FROM tbl_productos p JOIN tbl_categorias c ON c.categoria_id = p.producto_categoria JOIN tbl_tiendas t ON t.tienda_id = p.producto_tienda JOIN tbl_usuarios u ON u.usuario_id = t.tienda_usuario WHERE p.producto_oferta > 0 and p.producto_publicacion BETWEEN %s and %s",(fecha_inicio,fecha_final))
      
      elif categoria !=None and (precio_menor!=None and precio_mayor!=None) and (fecha_inicio == None and fecha_final == None) :
        cursor.execute('SELECT p.producto_publicacion, p.producto_nombre,p.producto_descripcion, p.producto_precio, p.producto_oferta, c.categoria_nombre, u.usuario_nombre_compl FROM tbl_productos p JOIN tbl_categorias c ON c.categoria_id = p.producto_categoria  JOIN tbl_tiendas t ON t.tienda_id = p.producto_tienda  JOIN tbl_usuarios u ON u.usuario_id = t.tienda_usuario WHERE p.producto_oferta > 0 and c.categoria_id  = %s and  p.producto_oferta BETWEEN %s and %s',(categoria, precio_menor, precio_mayor))
      elif categoria !=None and (precio_menor==None and precio_mayor==None) and (fecha_inicio != None and fecha_final != None) :
        cursor.execute('SELECT p.producto_publicacion, p.producto_nombre,p.producto_descripcion, p.producto_precio, p.producto_oferta, c.categoria_nombre, u.usuario_nombre_compl FROM tbl_productos p JOIN tbl_categorias c ON c.categoria_id = p.producto_categoria  JOIN tbl_tiendas t ON t.tienda_id = p.producto_tienda  JOIN tbl_usuarios u ON u.usuario_id = t.tienda_usuario WHERE p.producto_oferta > 0 and c.categoria_id  = %s and  p.producto_publicacion BETWEEN %s and %s',(categoria, fecha_inicio, fecha_final))

      elif (precio_menor!=None and precio_mayor!=None) and categoria == None and (fecha_inicio != None and fecha_final != None)  :
        cursor.execute("SELECT p.producto_publicacion, p.producto_nombre,p.producto_descripcion, p.producto_precio, p.producto_oferta, c.categoria_nombre, u.usuario_nombre_compl FROM tbl_productos p JOIN tbl_categorias c ON c.categoria_id = p.producto_categoria  JOIN tbl_tiendas t ON t.tienda_id = p.producto_tienda  JOIN tbl_usuarios u ON u.usuario_id = t.tienda_usuario WHERE p.producto_oferta > 0 and p.producto_oferta BETWEEN %s and %s  and p.producto_publicacion BETWEEN %s and %s",(precio_menor, precio_mayor, fecha_inicio, fecha_final))
      else:
        cursor.execute("SELECT p.producto_publicacion, p.producto_nombre,p.producto_descripcion, p.producto_precio, p.producto_oferta,  c.categoria_nombre, u.usuario_nombre_compl FROM tbl_productos p JOIN tbl_categorias c ON c.categoria_id = p.producto_categoria  JOIN tbl_tiendas t ON t.tienda_id = p.producto_tienda  JOIN tbl_usuarios u ON u.usuario_id = t.tienda_usuario WHERE p.producto_oferta > 0 and c.categoria_id  = %s and p.producto_oferta BETWEEN  %s and %s and p.producto_publicacion BETWEEN %s and %s",(categoria, precio_menor, precio_mayor, fecha_inicio, fecha_final))
      
      result=cursor.fetchall()

      return ('ok', result)
  except  Exception as ex:
        return ('error',repr(ex))