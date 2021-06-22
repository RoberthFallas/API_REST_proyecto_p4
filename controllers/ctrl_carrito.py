from flask import json, jsonify, request, flash, redirect, url_for
from init import app
from werkzeug.utils import secure_filename
from services import srv_carrito

@app.route('/get_miCarrito/<int:idCliente>')        
def get_miCarrito(idCliente):
        resp=srv_carrito.get_miCarrito(idCliente)
        json_items=[]
        content={}
        for resul in resp:
            content={'producto':resul[0],'nombre':resul[1],'descripcion':resul[2],'foto':resul[3],'cantidad':resul[4]}
            json_items.append(content)
            content={}
        return jsonify(json_items)

@app.route('/agregar_carrito',methods=['POST']) 
def agregar_carrito():
     _json=request.get_json(force=True)
     resp=srv_carrito.agregar_carrito(_json)
     resp = jsonify('suscripcion Guardada.')
     resp.status_code = 200
     return resp
     
@app.route('/eliminar_carrito/<int:idComprador>/<int:idProducto>',methods=['DELETE']) 
def eliminar_carrito(idComprador,idProducto):
     resp=srv_carrito.eliminar_carrito(idComprador,idProducto)
     return resp