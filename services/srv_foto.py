from pymysql.cursors import Cursor
from init import mysql
from contextlib import closing
from werkzeug.security import generate_password_hash, check_password_hash



def save_photo(id_producto,name):
 try:
        conect = mysql.connect()

        query = "INSERT INTO tbl_fotos(foto_producto, foto_url) VALUES (%s, %s)"
      

        data = (id_producto, name)

        with closing(conect.cursor()) as cursor:

            cursor.execute(query, data)
            conect.commit()

            return ('ok', 'foto correctamente guardada')

           
 except Exception as ex:
        return ('error', repr(ex))
     
