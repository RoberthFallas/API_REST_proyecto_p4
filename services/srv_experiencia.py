from flask.json import jsonify
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


def get_calficacionProducto(idUsuario,idProducto):
    try:
        conect = mysql.connect()
        with  closing(conect.cursor()) as cursor:
            cursor.execute('SELECT t.evaluacion_estrellas FROM tbl_evaluacion_productos t WHERE t.comprador_id=%s and t.producto_id=%s', (idUsuario,idProducto))
            result=cursor.fetchall()
            return (result)
    except Exception as ex:
        return ('error', repr(ex))

def get_comprador(id):
    try:
        conect = mysql.connect()
        with  closing(conect.cursor()) as cursor:
            cursor.execute('SELECT c.comprador_id FROM tbl_compradores c  where c.comprador_usuario=%s', (id))
            result=cursor.fetchall()
            return (result)
    except Exception as ex:
        return ('error', repr(ex))

def set_calificacion(json_data):
    try:
        conect = mysql.connect()

        query = "INSERT INTO tbl_evaluacion_productos (comprador_id,producto_id,evaluacion_estrellas) VALUES (%s,%s,%s)"
        _idComprador= json_data['idComprador']
        _idProducto = json_data['idProducto']
        _calificacion = json_data['calificacion']

        data = (_idComprador, _idProducto,_calificacion)

        with closing(conect.cursor()) as cursor:

            cursor.execute(query, data)
            conect.commit()
            id_insert =  cursor.lastrowid 
            resp=('ok', id_insert)
            return resp
    except  Exception as ex:
        return ('error', repr(ex))

            
            
def editat_calificacion(json_data):
      _idComprador= json_data['idComprador']
      _idProducto = json_data['idProducto']
      _calificacion = json_data['calificacion']
      query = "UPDATE tbl_evaluacion_productos SET evaluacion_estrellas=%s WHERE comprador_id=%s and producto_id=%s"
      data=(_calificacion,_idComprador,_idProducto)
      conn = mysql.connect()
      cur = conn.cursor()
      cur.execute(query, data)
      conn.commit()
      res = jsonify('Producto actualizado exitosamente.')
      res.status_code = 200
      return res


#Calificar tienda 
def insert_calificacion_tienda(json_data):
 try:
        conect = mysql.connect()

        query = "INSERT INTO tbl_evaluacion_tiendas (comprador_id,tienda_id,evaluacion_estrellas) VALUES (%s,%s,%s)" 

        _comprador= json_data['idComprador']
        _tienda = json_data['idTienda']
        _calificacion = json_data['calificacion']

        data = (_comprador, _tienda,_calificacion)

        with closing(conect.cursor()) as cursor:

            cursor.execute(query, data)
            conect.commit()

            id_insert =  cursor.lastrowid 

            return ('ok', id_insert)

           
 except Exception as ex:
        return ('error', repr(ex))


def get_calficacionTienda(idUsuario,idTienda):
    try:
        conect = mysql.connect()
        with  closing(conect.cursor()) as cursor:
            cursor.execute('SELECT t.evaluacion_estrellas FROM tbl_evaluacion_tiendas t WHERE t.comprador_id=%s and t.tienda_id=%s', (idUsuario,idTienda))
            result=cursor.fetchall()
            return (result)
    except Exception as ex:
        return ('error', repr(ex))


def set_calificacion_tienda(json_data):
    try:
        conect = mysql.connect()

        query = "INSERT INTO tbl_evaluacion_tiendas (comprador_id,tienda_id,evaluacion_estrellas) VALUES (%s,%s,%s)"
        _idComprador= json_data['idComprador']
        _idTienda = json_data['idTienda']
        _calificacion = json_data['calificacion']

        data = (_idComprador, _idTienda,_calificacion)

        with closing(conect.cursor()) as cursor:

            cursor.execute(query, data)
            conect.commit()
            id_insert =  cursor.lastrowid 
            resp=('ok', id_insert)
            return resp
    except  Exception as ex:
        return ('error', repr(ex))

            
            
def editat_calificacion_tienda(json_data):
      _idComprador= json_data['idComprador']
      _idTienda = json_data['idTienda']
      _calificacion = json_data['calificacion']
      query = "UPDATE tbl_evaluacion_tiendas SET evaluacion_estrellas=%s WHERE comprador_id=%s and tienda_id=%s"
      data=(_calificacion,_idComprador,_idTienda)
      conn = mysql.connect()
      cur = conn.cursor()
      cur.execute(query, data)
      conn.commit()
      res = jsonify('Producto actualizado exitosamente.')
      res.status_code = 200
      return res

