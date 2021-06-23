
from flask.json import jsonify
from pymysql.cursors import Cursor
from init import mysql
from contextlib import closing

def get_comentarios(id):
    try:
        conect = mysql.connect()
        with  closing(conect.cursor()) as cursor:
            'cursor.execute(''SELECT t.coment_id,t.coment_comprador,t.coment_cuerpo,t.coment_publicacion,u.usuario_foto,u.usuario_nom_usr FROM tbl_comentarios t INNER JOIN tbl_compradores c on c.comprador_id=t.coment_comprador INNER JOIN tbl_usuarios u on u.usuario_id=c.comprador_usuario  WHERE t.coment_producto=%s ORDER BY t.coment_id desc'', (id))'
            cursor.execute('SELECT t.coment_id,t.coment_comprador,t.coment_cuerpo,t.coment_publicacion,u.usuario_foto,u.usuario_nom_usr,r.resp_cuerpo FROM tbl_comentarios t INNER JOIN tbl_compradores c on c.comprador_id=t.coment_comprador INNER JOIN tbl_usuarios u on u.usuario_id=c.comprador_usuario LEFT JOIN tbl_respuestas r on r.resp_comenrario=t.coment_id WHERE t.coment_producto=%s ORDER BY t.coment_id desc',(id))
            result=cursor.fetchall()
            return (result)
    except Exception as ex:
        return ('error', repr(ex))

def set_comentario(json_data):
    try:
        conect = mysql.connect()
        query = "INSERT INTO tbl_comentarios(coment_comprador,coment_producto,coment_cuerpo,coment_publicacion) VALUES (%s,%s,%s,%s)"
        _idComprador= json_data['idComprador']
        _idProducto = json_data['idProducto']
        _fecha= json_data['fecha']
        _comentario = json_data['comentario']

        data = (_idComprador, _idProducto,_comentario,_fecha)

        with closing(conect.cursor()) as cursor:

            cursor.execute(query, data)
            conect.commit()
            id_insert =  cursor.lastrowid 
            resp=('ok', id_insert)
            return resp
    except  Exception as ex:
        return ('error', repr(ex))

def eliminar_comentario(idComprador,idProducto,idMensaje):
    try:
        conect = mysql.connect()
        with  closing(conect.cursor()) as cursor:
            cursor.execute('DELETE FROM tbl_comentarios where tbl_comentarios.coment_comprador=%s and tbl_comentarios.coment_producto=%s and tbl_comentarios.coment_id=%s', (idComprador,idProducto,idMensaje))
            conect.commit()
            res=jsonify('Comentario eliminado correctamente')
            return res
    except Exception as ex:
        return ('error', repr(ex))


def get_comentarios_tienda(id):
    try:
        conect = mysql.connect()
        with  closing(conect.cursor()) as cursor:
            cursor.execute('SELECT coment_id, coment_comprador, coment_producto, coment_cuerpo, coment_publicacion,u.usuario_foto,u.usuario_nom_usr, r.resp_cuerpo, p.producto_nombre, f.foto_url FROM tbl_comentarios c JOIN tbl_productos p ON p.producto_id = c.coment_producto JOIN tbl_fotos f ON f.foto_id = (SELECT ff.foto_id FROM tbl_fotos ff WHERE ff.foto_producto = p.producto_id LIMIT 1) JOIN tbl_compradores cp ON cp.comprador_id = c.coment_comprador JOIN tbl_usuarios u ON u.usuario_id = cp.comprador_usuario JOIN tbl_tiendas t ON p.producto_tienda = t.tienda_id LEFT JOIN tbl_respuestas r ON r.resp_comenrario = c.coment_id WHERE r.resp_cuerpo IS NULL AND t.tienda_id = %s',(id)) 
            result=cursor.fetchall()
            print(result)
            return ('ok', result)
    except Exception as ex:
        return ('error', repr(ex))