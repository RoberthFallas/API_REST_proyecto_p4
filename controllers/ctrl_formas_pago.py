import random
from init import app
from flask.json import jsonify, request
from services import srv_formas_pago
from services import srv_compradores


@app.route('/get_formas_pago_by_user_id/<int:id>', methods=['GET'])
def get_metodos_pago_by_user_id(id):
    try:
        resp = srv_formas_pago.get_metodos_by_user_id(id)
        if resp[0] is 'ok':
            ouput = list()

            for row in resp[1]:
                json = {'pago_id': row[0], 'propietario': row[1], 'tarjeta': row[2],
                 'vencimiento': row[3], 'pago_saldo': row[4]}
                ouput.append(json)
            return jsonify(ouput)
        else:
            response = jsonify(resp[1])
            response.status_code = 204 if resp[0] == 'warn' else 500
            return response
    except Exception as ex:
        print(ex)


@app.route('/create_forma_pago', methods=['POST'])
def create_forma_pago():
    try:
        _json = request.get_json(force=True)
        comprador_id = srv_compradores.get_comprador_id_by_user_id(_json['usuario_id'])
        if comprador_id[0] is 'ok':

            array = (comprador_id[1], _json['pago_nomb_duenno'],_json['pago_numero_tarjeta'],_json['pago_cvv'],
            _json['pago_vencimiento'], random.randrange(10000000))
            resp = srv_formas_pago.create_forma_pago(array)

            if resp[0] is 'ok':
                return jsonify("Forma de pago guardada")
            else:
                response = jsonify("Un erro inesperado a ocacionado que se puedan guardar tus datos")
                response.status_code = 500
                return response
        else:
            response = jsonify(resp[1])
            response.status_code = 409
            return response
    except Exception as ex:
        print(ex)


@app.route('/hide_forma_pago_by_id', methods=['PUT'])
def hide_forma_pago_by_id():
    try:
        _json = request.get_json(force=True)
        resp = srv_formas_pago.hide_forma_pago(_json['pago_id'])
        if resp[0] is 'ok':
            return jsonify('Forma de pago eliminada')
        else:
            response = jsonify(resp[1])
            response.status_code = 409
            return response
    except Exception as ex:
        print(ex)

@app.route('/agregar_bonificacion_by_id', methods=['PUT'])
def agregar_bonificacion():
    try:
        _json = request.get_json(force=True)
        resp = srv_formas_pago.agregar_bonificacion(_json['pago_id'])
        if resp[0] is 'ok':
            return jsonify('Bonificación remunerada')
        else:
            response = jsonify(resp[1])
            response.status_code = 409
            return response
    except Exception as ex:
        print(ex)

