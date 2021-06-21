from init import app
from flask.json import jsonify, request
from services import srv_compradores
from services import srv_direccion
from services import srv_direccion_envio


@app.route('/create_direccion_envio', methods=['POST'])
def create_direccion_envio():
    try:
        _json = request.get_json(force=True)
        comprador_id = srv_compradores.get_comprador_id_by_user_id(_json['usuario_id'])
        if comprador_id[0] is 'ok':
            dir_array = (_json['direcciion_pais'], _json['direccion_provincia'], _json['direccion_canton'])
            resp = srv_direccion.create_direccion(dir_array)

            envio_array = (comprador_id[1], resp[1], _json['envio_cod_postal'], _json['envio_casillero'], _json['envio_observaciones'])
            
            srv_direccion_envio.create_direccion_envio(envio_array)

            return jsonify("Dirección de envío guardada")
        else:
            response = jsonify(resp[1])
            response.status_code = 409
            return response
    except Exception as ex:
        print(ex)



@app.route('/get_direcciones_envio_by_user_id/<int:id>', methods=['GET'])
def get_direcciones_envio_by_user_id(id):
    try:
        resp = srv_direccion_envio.get_full_direccion_by_user_id(id)
        if resp[0] is 'ok':
            ouput = list()

            for row in resp[1]:
                json = {'envio_id': row[0], 'país': row[1], 'provincia': row[2],
                        'cantón': row[3], 'direccion_id': row[4], 'cod postal': row[5],
                        'casillero': row[6]}
                ouput.append(json)
            return jsonify(ouput)
        else:
            response = jsonify(resp[1])
            response.status_code = 204 if resp[0] == 'warn' else 500
            return response
    except Exception as ex:
        print(ex)


@app.route('/hide_direccion_envio_by_id', methods=['PUT'])
def hide_direccion_envio_by_id():
    try:
        _json = request.get_json(force=True)
        resp = srv_direccion_envio.hide_direccion_envio(_json['envio_id'])
        if resp[0] is 'ok':
            return jsonify('Direccionón de envio eliminada')
        else:
            response = jsonify(resp[1])
            response.status_code = 409
            return response
    except Exception as ex:
        print(ex)