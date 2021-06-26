from flask import Flask
from flask_cors import CORS
from flaskext.mysql import MySQL

UPLOAD_FOLDER = '/resources/images'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)

mysql = MySQL()

# MySQL configs
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'bd_proyecto_p4'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

from controllers import ctrl_test
from controllers import ctrl_usuario
from controllers import ctrl_authentication
from controllers import ctrl_producto
from controllers import ctrl_categoria
from controllers import ctrl_tienda
from controllers import ctrl_fotos
from  controllers import  ctrl_experiencia
from  controllers import  ctrl_comentarios
from controllers import  ctrl_suscripciones
from controllers import  ctrl_reporteAbuso
from controllers import  ctrl_deseo
from controllers import  ctrl_carrito
from controllers import  ctrl_compra
from controllers import ctrl_comprador
from controllers import ctrl_formas_pago
from controllers import crtl_direccion_envio
from controllers import ctrl_facturas
from controllers import ctrl_redes_sociales