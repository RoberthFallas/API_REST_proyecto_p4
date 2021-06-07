from flask.json import jsonify, request
from werkzeug.wrappers import response
from init import app
from services import srv_usuario
from services import srv_direcciones
from services import srv_tiendas


@app.route('/create_usuario', methods=['POST'])
def create_usuario():
    try:
        _json = request.get_json(force=True)

        user_list = (_json['usuario_nom_urs'], _json['usuario_contrasena'], _json['usuario_email'], 'unknow.jpg', _json['usuario_telefono'],
            _json['usuario_cedula'], _json['usuario_nombre_compl'], _json['usuario_tipo'])
        usr_result = srv_usuario.create_usuario(user_list)

        dir_list = (_json['direcciion_pais'],  _json['direccion_provincia'], _json['direccion_canton'])
        dir_result = srv_direcciones.create_direccion(dir_list)

        if _json['usuario_tipo'] == 'T':
            srv_direcciones.create_direccion((usr_result[1], dir_result[1], _json['descripcion']))

        response = jsonify("Usuario creado de manera exitosa")
        return response
    except Exception as e:
        print(e)