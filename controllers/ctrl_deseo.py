from flask import json, jsonify, request, flash, redirect, url_for
from init import app
from werkzeug.utils import secure_filename
from services import srv_deseos

@app.route('/get_deseo/<int:idCliente>/<int:idProducto>')        
def get_deseo(idCliente,idProducto):
        resp=srv_deseos.get_deseo(idCliente,idProducto)
        json_items=[]
        content={}
        for resul in resp:
            content={'cliente':resul[0],'producto':resul[1]}
            json_items.append(content)
            content={}
        return jsonify(json_items)

@app.route('/agregar_deseo',methods=['POST']) 
def agregar_deseo():
     _json=request.get_json(force=True)
     resp=srv_deseos.insertar_deseo(_json)
     resp = jsonify('suscripcion Guardada.')
     resp.status_code = 200
     return resp

@app.route('/eliminar_deseo/<int:idComprador>/<int:idProducto>',methods=['DELETE']) 
def eliminar_deseo(idComprador,idProducto):
     resp=srv_deseos.eliminar_deseo(idComprador,idProducto)
     return resp

@app.route('/get_misDeseos/<int:idCliente>')        
def get_misDeseos(idCliente):
        resp=srv_deseos.get_misDeseos(idCliente)
        json_items=[]
        content={}
        for resul in resp:
            content={'producto':resul[0],'nombre':resul[1],'descripcion':resul[2],'foto':resul[3]}
            json_items.append(content)
            content={}
        return jsonify(json_items)