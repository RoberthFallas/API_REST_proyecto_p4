from flask import json, jsonify
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
  