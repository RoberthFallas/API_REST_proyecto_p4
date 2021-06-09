from flask import Flask
from flask_cors import CORS
from flaskext.mysql import MySQL

app = Flask(__name__)
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
from controllers import ctrl_tienda