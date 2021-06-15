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
    # try:
    #     cur.execute('SELECT p.id_proveedor, p.codigo, p.nombre, p.telefono, p.correo, COUNT(pr.id) as nm_prodcs FROM tbl_proveedores p ' 
    #     +'LEFT JOIN tbl_productos pr ON pr.id_provedor = p.id_proveedor '
    #     +'WHERE p.id_proveedor <> 1 '
    #     +'GROUP BY p.codigo')
        
    #     json_items = []
    #     content = {}

    #     for result in rows:
    #         content = {'id_proveedor':result[0], 'codigo': result[1], 'nombre': result[2], 'telefono': result[3], 'correo': result[4], 'np_prodcs': result[5]}
    #         json_items.append(content)
    #         content = {}
    #     return jsonify(json_items)
    # except Exception as ex:
    #     print(ex)
    with closing(mysql.connect().cursor()) as cursor:
        try:
            cursor.execute('SELECT COUNT(u.usuario_id) FROM tbl_usuarios u WHERE (u.usuario_cedula = %s OR u.usuario_nom_usr = %s)', datos)
            rows = cursor.fetchone()
            resp = ('ok', rows[0])
            return resp
        except Exception as ex:
            return ('error', repr(ex))

