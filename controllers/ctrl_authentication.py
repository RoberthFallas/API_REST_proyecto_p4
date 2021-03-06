from flask import json, jsonify
from werkzeug.wrappers import response
from init import app
from services import srv_authentication




@app.route('/getTiendaByUserId/<string:user_id>')
def getTiendaByUser(user_id):
    try:
        response = None
        resp = srv_authentication.getTiendaByUserId(user_id)
        print('sshhs')
        print(resp[0])
        if resp[0] == 'ok':  
            print("entro ")                                                                                   #En la posicion 0 viene el estado en la 1 viene la lista de datos o el mensaje del error
            json = {'tienda_id':resp[1][0], 'tienda_descripcion':resp[1][1], 'tienda_pais':resp[1][2], 'tienda_provincia':resp[1][3],  'tienda_canton':resp[1][4],
                    'usuario_nombre':resp[1][5], 'usuario_foto':resp[1][6],'usuario_email':resp[1][7], 'usuario_telefono':resp[1][8],'usuario_cedula':resp[1][9],
                    'usuario_nombre_completo':resp[1][10]}

            print(json)
            response = jsonify(json)
            response.status_code = 200
        else:
            response = jsonify(resp[1])
            response.status_code = 401 if resp[0] == 'warn' else 500
        return response
    except Exception as ex:
        response = jsonify(repr(ex))
        response.status_code = 500
        return response 

@app.route('/login/<string:user>/<string:passw>')
def login(user, passw):
    try:
        response = None
        resp = srv_authentication.login(user, passw)

        print(resp)
        if resp[0] == 'ok':                                                                                     #En la posicion 0 viene el estado en la 1 viene la lista de datos o el mensaje del error
            json = {'usuario_id':resp[1][0], 'usuario_nom_usr':resp[1][1],'usuario_contrasenna':resp[1][2], 'usuario_email':resp[1][3],
                'usuario_foto':resp[1][4], 'usuario_telefono':resp[1][5], 'usuario_cedula':resp[1][6], 'usuario_nombre_compl':resp[1][7],
                'usuario_tipo':resp[1][8]}
            response = jsonify(json)
            response.status_code = 200
        else:
            response = jsonify(resp[1])
            response.status_code = 401 if resp[0] == 'warn' else 500
        return response
    except Exception as ex:
        response = jsonify(repr(ex))
        response.status_code = 500
        return response

