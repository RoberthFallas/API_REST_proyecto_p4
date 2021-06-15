
from flask import json, jsonify, send_file
from init import app
from services import srv_foto
import os
@app.route('/get_fotos_by_producto/<string:id>' )
def get_fotos_by_producto(id): 
      try:
        print("in get by id")
        response = None
        resp = srv_foto.getFotosProductosById(id)
        print(resp)
        if resp[0] == 'ok':     
            rows = resp[1]
            content = {}    
            json_items = []
            for result in rows:
                content = {'url': result[0]}
                json_items.append(content)
                content = {}
            response = jsonify(rows)
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


@app.route('/get_foto/<path:filename>')
def get_fotoo(filename):
    file_path = os.getcwd() + '/resources/images/' + filename
    return send_file(file_path)