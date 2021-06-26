from init import app
from flask import json
from flask.json import jsonify, request
from services import srv_redes_sociales



@app.route('/get_redes_sociales/<int:id>')
def get_redes_sociales(id):
    try:
        resp = srv_redes_sociales.get_redes_sociales(id)

        if(resp[0] == 'ok'):
            ouput = list()
            for row in resp[1]:
                json = {'red_id':row[0], 'red_nombre': row[1], 'red_direccion': row[2]}
                ouput.append(json)
            return jsonify(ouput)
           
        response = jsonify('No fue posible obtener los datos.')
        response.status_code = 500
        return response

    except Exception as ex:
        response = jsonify(repr(ex))
        response.status_code = 500
        return response



@app.route('/create_update_redes_sociales', methods=['POST'])
def create_update_redes_sociales():
    try:
        _json = request.get_json(force=True)
        array = _json['body']

        for item in array:
            if 'red_nombre' in item:
                if 'red_id' not in item:
                    srv_redes_sociales.create_red_social((_json['user_id'], item['red_nombre'], item['red_direccion']))
                else:
                    srv_redes_sociales.update_red_social(item['red_id'], item['red_direccion'])
        return(jsonify('Cambios exitosos'))
    except Exception as ex:
        response = jsonify(repr(ex))
        response.status_code = 500
        return response
