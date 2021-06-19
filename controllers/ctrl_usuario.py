import os
from flask import json
from werkzeug.utils import secure_filename
from flask.json import jsonify, request
from init import app
from services import srv_usuario
from services import srv_direccion
from services import srv_tiendas
from services import srv_compradores
from services import srv_direccion_envio

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
PROFILES_FOLDER = '/resources/images/profiles/'


@app.route('/create_usuario', methods=['POST'])
def create_usuario():
    try:
        str_data = request.form['string_data']
        _json = json.loads(str_data)

        if check_user_data(_json['usuario_cedula'], _json['usuario_nom_urs']):

            user_list = (_json['usuario_nom_urs'], _json['usuario_contrasena'], _json['usuario_email'],
                         save_profile_pictore(
                             _json['usuario_nom_urs']), _json['usuario_telefono'],
                         _json['usuario_cedula'], _json['usuario_nombre_compl'], _json['usuario_tipo'])
            usr_result = srv_usuario.create_usuario(user_list)

            dir_list = (_json['direcciion_pais'],
                        _json['direccion_provincia'], _json['direccion_canton'])
            dir_result = srv_direccion.create_direccion(dir_list)

            if _json['usuario_tipo'] == 'T':
                srv_tiendas.create_tienda(
                    (usr_result[1], dir_result[1], _json['tienda_descripcion']))
            else:
                com_result = srv_compradores.create_comprador(usr_result[1])
                srv_direccion_envio.create_direccion_envio((com_result[1], dir_result[1],
                                                            _json['envio_cod_postal'], _json['envio_casillero'], _json['envio_observaciones']))
            response = jsonify("Usuario creado de manera exitosa")
            return response
        else:
            response = jsonify(
                "El nombre de usuario o cédula que has ingresado ya están en uso.")
            response.status_code = 409
            return response
    except Exception as e:
        print(e)


def check_user_data(cedula, nombre_usuario):
    counted = srv_usuario.check_user_data((cedula, nombre_usuario))
    return counted[1] == 0


def save_profile_pictore(user_name):
    file = request.files.get('file')
    if file is not None:
        try:
            if allowed_file(file.filename):
                filname = secure_filename(user_name + '.' + file.filename.rsplit('.', 1)[1].lower())
                file.save(os.getcwd() + PROFILES_FOLDER + filname)
                return filname
        except Exception:
            pass
    return 'unknow.jpg'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/get_userdata_by_id/<int:id>', methods=['GET'])
def get_userdata_by_id(id):
    try:
        resp = srv_usuario.get_usuario_by_id(id)
        if resp[0] is "ok":
            _json = {"usuario_id": resp[1][0], "usuario_nom_usr":resp[1][1],
             "usuario_email": resp[1][3], "usuario_foto":resp[1][4],
             "usuario_telefono": resp[1][5], "usuario_cedula":resp[1][6],
             "usuario_nombre_compl": resp[1][7], "usuario_tipo":resp[1][8]}
            return jsonify(_json)
        else:
            response = jsonify(resp[1])
            response.status_code = 204 if resp[0] == 'warn' else 500
            return response
    except Exception as ex:
        print(ex)
