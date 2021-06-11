from pymysql.cursors import Cursor
from init import mysql
from contextlib import closing
from werkzeug.security import generate_password_hash, check_password_hash




'''def login(user, password):
    try:
        conect = mysql.connect()
        with closing(conect.cursor()) as cursor:

            cursor.execute('SELECT u.usuario_id, u.usuario_contrasenna, u.usuario_tipo FROM tbl_usuarios u WHERE u.usuario_nom_usr=%s', (user,))

            
            if cursor.rowcount > 1:
                return ('error', 'Vaya, no es posible iniciar sesion con tu cuenta, comunicate con soporte para solucionar este inconveniente. (Usuarios repetidos)')
            else:
                result = cursor.fetchone()
                if result:
                    db_password = result[1]
                    if check_password_hash(db_password, password):
                        cursor.execute('SELECT u.*, t.tienda_id, t.tienda_descripcion, d.direcciion_pais, d.direccion_canton  FROM tbl_usuarios u  JOIN  tbl_tiendas t ON t.tienda_usuario = u.usuario_id  JOIN tbl_direcciones d ON t.tienda_direccion = d.direccion_id WHERE u.usuario_id=%s', (result[0],))
                        return ('ok', cursor.fetchone())
                    else:
                        return ('warn', 'La contraseña que has ingresado no corresponde con tu usuario')
                else:
                    return ('warn', 'Lo sentimos, no existe el usuario que has especificado')
    except Exception as ex:
        return ('error', repr(ex))'''
def login(user, password):
    try:
        conect = mysql.connect()
        with closing(conect.cursor()) as cursor:

            cursor.execute('SELECT u.usuario_id, u.usuario_contrasenna, u.usuario_tipo FROM tbl_usuarios u WHERE u.usuario_nom_usr=%s', (user,))

            
            if cursor.rowcount > 1:
                return ('error', 'Vaya, no es posible iniciar sesion con tu cuenta, comunicate con soporte para solucionar este inconveniente. (Usuarios repetidos)')
            else:
                result = cursor.fetchone()
                if result:
                    db_password = result[1]
                    if check_password_hash(db_password, password):
                        cursor.execute('SELECT u.* FROM tbl_usuarios u WHERE u.usuario_id=%s', (result[0],))
                        return ('ok', cursor.fetchone())
                    else:
                        return ('warn', 'La contraseña que has ingresado no corresponde con tu usuario')
                else:
                    return ('warn', 'Lo sentimos, no existe el usuario que has especificado')
    except Exception as ex:
        return ('error', repr(ex))