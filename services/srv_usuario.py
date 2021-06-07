from init import mysql
from contextlib import closing
from werkzeug.security import generate_password_hash
#from werkzeug.security import check_password_hash -----> si se necesita comprobar contrasenna


def  create_usuario(datos):
    try:
        data = list()
        data.extend(datos)
        conect = mysql.connect()
        with closing(conect.cursor()) as cursor:
            
            data[1] = generate_password_hash(data[1])
            cursor.execute('INSERT INTO tbl_usuarios(usuario_nom_usr, usuario_contrasenna, usuario_email, usuario_foto,' 
                +'usuario_telefono, usuario_cedula, usuario_nombre_compl, usuario_tipo) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)', data)

            conect.commit()
            resp = ('ok', cursor.lastrowid)
            return resp
    except Exception as ex:
        return ('error', repr(ex))


def create_compradores(datos):
    try:
        conect = mysql.connect()
        with closing(conect.cursor()) as cursor:
            cursor.execute('INSERT INTO tbl_compradores(comprador_usuario) VALUES(%s)', datos)
            conect.commit()
            resp = ('ok', '')
            return resp
    except Exception as ex:
        return ('error', repr(ex))
