from flask import json, jsonify, request, flash, redirect, url_for
from init import app
from werkzeug.utils import secure_filename
from services import srv_suscripciones
#obtiene 
@app.route('/get_suscripcion/<int:idCliente>/<int:idTienda>')        
def get_subscripcion(idCliente,idTienda):
        resp=srv_suscripciones.get_suscripcion(idCliente,idTienda)
        json_items=[]
        content={}
        for resul in resp:
            content={'cliente':resul[0],'tienda':resul[1]}
            json_items.append(content)
            content={}
        return jsonify(json_items)

#Agregar suscripciones 
@app.route('/agregar_suscripcion',methods=['POST']) 
def agregar_suscripcion():
     _json=request.get_json(force=True)
     resp=srv_suscripciones.insertar_suscripcion(_json)
     resp = jsonify('suscripcion Guardada.')
     resp.status_code = 200
     return resp
 
 #eliminar  las suscripciones mediante id
@app.route('/eliminar_suscripcion/<int:idComprador>/<int:idTienda>',methods=['DELETE']) 
def eliminar_suscripcion(idComprador,idTienda):
     resp=srv_suscripciones.eliminar_suscripcion(idComprador,idTienda)
     return resp

 #obtiene las suscripciones de los clientes mediante id
@app.route('/get_miSuscripcion/<int:idCliente>')        
def get_miSuscripcion(idCliente):
        resp=srv_suscripciones.get_miSuscripcion(idCliente)
        json_items=[]
        content={}
        for resul in resp:
            content={'tienda':resul[0],'nombre':resul[1],'foto':resul[2]}
            json_items.append(content)
            content={}
        return jsonify(json_items)
