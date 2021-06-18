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



def create_direccion(data_list):
    try:
        conect = mysql.connect()
        with closing(conect.cursor()) as cursor:
            cursor.execute('INSERT INTO tbl_direcciones(direcciion_pais, direccion_provincia, direccion_canton) VALUES(%s, %s, %s)', data_list)
            conect.commit()
            resp = ('ok', cursor.lastrowid)
            return resp
    except Exception as ex:
        return ('error', repr(ex))
     