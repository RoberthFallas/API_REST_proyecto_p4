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
            content={'producto':resul[0],'nombre':resul[1],'descripcion':resul[2],'foto':resul[3],'cantidad':resul[4],'precio':resul[5]}
            json_items.append(content)
            content={}
        return jsonify(json_items)

@app.route('/agregar_carrito',methods=['POST']) 
def agregar_carrito():
     _json=request.get_json(force=True)
     resp=srv_carrito.agregar_carrito(_json)
     if resp=='ok':
        resp = jsonify('producto Guardado.')
        resp.status_code = 200
     else:
         resp=srv_carrito.editar_carritoSuma(_json)
         aux=int(_json['cantidad'])
         aux2= (resp[0])
         _json['cantidad']=aux+aux2
         srv_carrito.editar_carrito(_json)
         resp = jsonify('producto Editado.')
         resp.status_code = 200
     return resp

@app.route('/eliminar_carrito/<int:idComprador>/<int:idProducto>',methods=['DELETE']) 
def eliminar_carrito(idComprador,idProducto):
     resp=srv_carrito.eliminar_carrito(idComprador,idProducto)
     return resp

@app.route('/editar_carrito', methods=['PUT']) #Sólo podrá ser accedida vía PUT
def editar_carrito():
    _json=request.get_json(force=True)
    resp=srv_carrito.editar_carrito(_json)
    resp = jsonify('producto editado.')
    resp.status_code = 200