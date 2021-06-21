from init import mysql
from contextlib import closing
from werkzeug.security import generate_password_hash

def get_metodos_by_user_id(id):
    with closing(mysql.connect().cursor()) as cursor:
        try:
            cursor.execute('SELECT f.pago_id, f.pago_nomb_duenno, f.pago_numero_tarjeta, '
                        'f.pago_vencimiento, f.pago_saldo FROM tbl_formas_pago f '
                        'INNER JOIN tbl_compradores c ON c.comprador_id = f.pago_comprador '
                        'WHERE c.comprador_usuario = %s and f.pago_activa LIKE "V"', (id,))
            rows = cursor.fetchall()
            resp = ('ok', rows)
            return resp
        except Exception as ex:
            return ('error', repr(ex))


def create_forma_pago(datos):
    try:
        conect = mysql.connect()
        with closing(conect.cursor()) as cursor:
            cursor.execute('INSERT INTO tbl_formas_pago(pago_comprador, pago_nomb_duenno, '
                    'pago_numero_tarjeta, pago_cvv, pago_vencimiento, pago_saldo) '
                    'VALUES(%s,%s,%s,%s,%s,%s)', datos)
            conect.commit()
            resp = ('ok', '')
            return resp
    except Exception as ex:
        return ('error', repr(ex))

def get_comprador_id_by_user_id(id):
    with closing(mysql.connect().cursor()) as cursor:
        try:
            cursor.execute('SELECT c.comprador_id FROM tbl_compradores c '
            'WHERE c.comprador_usuario = %s', (id,))
            rows = cursor.fetchone()
            resp = ('ok', rows[0])
            return resp
        except Exception as ex:
            return ('error', repr(ex))


def hide_forma_pago(id):
    try:
        conect = mysql.connect()
        with closing(conect.cursor()) as cursor:
            cursor.execute('UPDATE tbl_formas_pago SET pago_activa = "F" WHERE pago_id = %s', (id,))
            conect.commit()
            resp = ('ok', '')
            return resp
    except Exception as ex:
        return ('error', repr(ex))