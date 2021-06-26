from flask.json import jsonify 
from pymysql.cursors import Cursor 
from init import mysql 
from contextlib import closing 
 
def create_giro_ruleta(json_data): 
 try: 
        conect = mysql.connect() 
        query = "INSERT INTO tbl_giros_ruleta(giro_cliente, giro_fecha, giro_resultado) VALUES (%s, CURRENT_DATE(), %s)"  
        _comprador= json_data['comprador_id'] 
        _resultado = json_data['resultado'] 
        data = (_comprador, _resultado) 
 
        with closing(conect.cursor()) as cursor: 
 
            cursor.execute(query, data) 
            conect.commit() 
             
            return ('ok') 
 except Exception as ex: 
        return ('error', repr(ex)) 
         
 
def get_regalías(comprador_id): 
 try: 
        conect = mysql.connect() 
        query = "INSERT INTO tbl_giros_ruleta(giro_cliente, giro_fecha, giro_resultado) VALUES (%s, CURRENT_DATE(), %s)"  
        _comprador= json_data['comprador_id'] 
        _resultado = json_data['resultado'] 
        data = (_comprador, _resultado) 
 
        with closing(conect.cursor()) as cursor: 
 
            cursor.execute(query, data) 
            
            return ('ok', cursor.fetchall()) 
 except Exception as ex: 
        return ('error', repr(ex)) 
 
def get_giros_hoy(comprador_id): 
 try: 
        conect = mysql.connect() 
        
        with closing(conect.cursor()) as cursor: 
            cursor.execute("SELECT COUNT(r.giro_id) FROM tbl_giros_ruleta r WHERE r.giro_fecha = CURRENT_DATE() and r.giro_cliente = %s", (comprador_id) ) 
            conect.commit() 
            return ('ok', cursor.fetchall()) 
 except Exception as ex: 
        return ('error', repr(ex))

def agregar_bonificacion(id):
    try:
        conect = mysql.connect()
        with closing(conect.cursor()) as cursor:
            cursor.execute('UPDATE tbl_formas_pago p SET pago_saldo = 25000 WHERE p.pago_id = %s', (id))
            conect.commit()
            resp = ('ok', '')
            return resp
    except Exception as ex:
        return ('error', repr(ex))