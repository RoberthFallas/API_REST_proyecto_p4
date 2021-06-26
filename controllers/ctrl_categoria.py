from flask import json, jsonify, request
from init import app
from services import srv_categoria

@app.route('/get_categorias')

def get_categorias():
    try:
        response = None
        resp = srv_categoria.get_categorias()
        print(resp)
        if resp[0] == 'ok':     
            rows = resp[1]
            print(rows)  
            content = {}    
            json_items = []
            for result in rows:
                content = {'value': result[0], 'text': result[1]}
                json_items.append(content)
                content = {}

            response = jsonify(json_items)
            response.status_code = 200
        else:
            response = jsonify(resp[1])
            response.status_code = 401 if resp[0] == 'warn' else 500
        print(response)
        return response
    except Exception as ex:
        response = jsonify(repr(ex))
        response.status_code = 500
        return response 


@app.route('/create_categoria', methods=['POST'])
def create_categoria():
    try:
        _json = request.get_json(force=True) 
        resp = srv_categoria.create_cateorias(_json)

        print(resp)
        if(resp == 'ok'):
            response = jsonify('Categoria guardada éxitosamente')
            response.status_code = 200
            return response

        response = jsonify('No se pudo guardar la categoría')
        response.status_code = 401
        return response

    except Exception as ex:
        response = jsonify(repr(ex))
        response.status_code = 500
        return response 


