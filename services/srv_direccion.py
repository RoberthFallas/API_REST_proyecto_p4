from pymysql.cursors import Cursor
from init import mysql
from contextlib import closing

def insert_direccion_producto(json_data):
 try:
        conect = mysql.connect()

        query = "INSERT INTO tbl_direcciones(direcciion_pais, direccion_provincia, direccion_canton) VALUES (%s,%s,%s)" 

        _pais = json_data['pais']
        _provincia = json_data['provincia']
        _canton = json_data['canton']

        data = (_pais, _provincia, _canton)

        with closing(conect.cursor()) as cursor:

            cursor.execute(query, data)
            conect.commit()

            id_insert =  cursor.lastrowid 

            return ('ok', id_insert)

           
 except Exception as ex:
        return ('error', repr(ex))
     
def update_direccion_producto(json_data):
 try:
        conect = mysql.connect()

        query = "UPDATE tbl_direcciones SET direcciion_pais=%s,direccion_provincia=%s,direccion_canton=%s WHERE direccion_id=%s" 
        _direccion_id = json_data['direccionId']      
        _pais = json_data['pais']
        _provincia = json_data['provincia']
        _canton = json_data['canton']

        data = ( _pais, _provincia, _canton, _direccion_id)

        with closing(conect.cursor()) as cursor:

            cursor.execute(query, data)
            conect.commit()
            return ('ok')

           
 except Exception as ex:
        return ('error', repr(ex))
     


