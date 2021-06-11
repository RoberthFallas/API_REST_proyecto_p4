from pymysql.cursors import Cursor
from init import mysql
from contextlib import closing
from werkzeug.security import generate_password_hash, check_password_hash



def get_categorias():
 try:
        conect = mysql.connect()

        query = "SELECT * FROM tbl_categorias" 

        with closing(conect.cursor()) as cursor:

            cursor.execute(query)
            rows = cursor.fetchall()
            return ('ok', rows)

           
 except Exception as ex:
        return ('error', repr(ex))
     