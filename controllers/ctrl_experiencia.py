from flask import json, jsonify, request, flash, redirect, url_for
from init import app
from werkzeug.utils import secure_filename
from services import srv_experiencia

@app.route('/get_calificacionProducto/<int:idUsuario>/<int:idProducto>')        
def get_calificacionProducto(idUsuario,idProducto):
        resp=srv_experiencia.get_calficacionProducto(idUsuario,idProducto)
        json_items=[]
        content={}
        for resul in resp:
            content={'calificacion':resul[0]}
            json_items.append(content)
            content={}
        return jsonify(json_items)

@app.route('/get_comprador2/<int:id>')        
def get_comprador2(id):
        resp=srv_experiencia.get_comprador(id)
        json_items=[]
        content={}
        for resul in resp:
            content={'comprador_id':resul[0]}
            json_items.append(content)
            content={}
        return jsonify(json_items)

@app.route('/calificar_producto',methods=['POST']) 
def calificar_producto():
     _json=request.get_json(force=True)
     resp=srv_experiencia.set_calificacion(_json)
     if resp[0]!='ok':
        srv_experiencia.editat_calificacion(_json)
     res = jsonify('Producto actualizado exitosamente.')
     res.status_code = 200
     return res

