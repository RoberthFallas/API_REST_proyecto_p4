from init import app
from services import srv_usuario
from flask import json
from flask.json import request, jsonify
from controllers import ctrl_usuario

@app.route('/edit_comprador', methods=['PUT'])
def edit_comprador():
    try:
        str_data = request.form['string_data']
        _json = json.loads(str_data)

        if ctrl_usuario.check_update_data(_json['usuario_id'], _json['usuario_cedula'], _json['usuario_nom_usr']):
            user_srv_list = (_json['usuario_nom_usr'], _json['usuario_email'], 
                ctrl_usuario.update_profile_pictore(request.files.get('file'), _json['usuario_nom_usr'], _json['usuario_foto']),  
                _json['usuario_telefono'], _json['usuario_cedula'], _json['usuario_nombre_compl'], _json['usuario_id'])
            
            result = srv_usuario.update_user(user_srv_list)

            if _json['usuario_contrasenna'] and result[0] is "ok":
                result = srv_usuario.change_password(_json['usuario_contrasenna'], _json['usuario_id'])

            if result[0] is "ok":
                return jsonify('Tus datos han sido actualizados')
            else:
                response = jsonify(result[1])
                response.status_code = 409
                return response
        else:
            response = jsonify("El nombre de usuario o cédula que has ingresado ya está en uso.")
            response.status_code = 409
            return response
    except Exception as ex:
        print(ex)