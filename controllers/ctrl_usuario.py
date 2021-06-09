from flask.json import jsonify, request
from werkzeug.wrappers import response
from init import app
from services import srv_usuario
from services import srv_direcciones
from services import srv_tiendas
from services import srv_compradores
from services import srv_direccion_envio


@app.route('/create_usuario', methods=['POST'])
def create_usuario():
    try:
        _json = request.get_json(force=True)

        if check_user_data(_json['usuario_cedula'], _json['usuario_nom_urs']):

            user_list = (_json['usuario_nom_urs'], _json['usuario_contrasena'], _json['usuario_email'], 'unknow.jpg', _json['usuario_telefono'],
                _json['usuario_cedula'], _json['usuario_nombre_compl'], _json['usuario_tipo'])
            usr_result = srv_usuario.create_usuario(user_list)

            dir_list = (_json['direcciion_pais'],  _json['direccion_provincia'], _json['direccion_canton'])
            dir_result = srv_direcciones.create_direccion(dir_list)

            if _json['usuario_tipo'] == 'T':
                srv_tiendas.create_tienda((usr_result[1], dir_result[1], _json['tienda_descripcion']))
            else:
                com_result = srv_compradores.create_comprador(usr_result[1])
                srv_direccion_envio.create_direccion_envio((com_result[1], dir_result[1], _json['envio_cod_postal'], _json['envio_casillero'], _json['envio_observaciones']))
            response = jsonify("Usuario creado de manera exitosa")
            return response
        else:
            response = jsonify("El nombre de usuario o cédula que has ingresado ya están en uso.")
            response.status_code = 409
            return response
    except Exception as e:
        print(e)


def check_user_data(cedula, nombre_usuario):
    counted = srv_usuario.check_user_data((cedula, nombre_usuario))
    return counted[1] == 0