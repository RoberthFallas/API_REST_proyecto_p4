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


def check_user_data(datos):
    with closing(mysql.connect().cursor()) as cursor:
        try:
            cursor.execute('SELECT COUNT(u.usuario_id) FROM tbl_usuarios u WHERE (u.usuario_cedula = %s OR u.usuario_nom_usr = %s)', datos)
            rows = cursor.fetchone()
            resp = ('ok', rows[0])
            return resp
        except Exception as ex:
            return ('error', repr(ex))

def get_usuario_by_id(id):
        with closing(mysql.connect().cursor()) as cursor:
            try:
                count = cursor.execute('select u.* from tbl_usuarios u where u.usuario_id = %s', (id,))
                if count is 1:
                    row = cursor.fetchone()
                    resp = ('ok', row)
                    return resp
                elif count is 0:
                    return ('warn', 'Sin coinsidencias para el parámetro de busqueda')
                else:
                    return ('error', 'Se ha cancelado la busqueda debido a que los resultados obtenidos contenian errores')
            except Exception as ex:
                return ('error', repr(ex))

