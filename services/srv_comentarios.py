from flask.json import jsonify
from pymysql.cursors import Cursor
from init import mysql
from contextlib import closing

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