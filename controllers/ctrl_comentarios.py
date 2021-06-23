from flask import json, jsonify, request, flash, redirect, url_for
from init import app
from werkzeug.utils import secure_filename
from services import srv_comentarios


@app.route('/get_comentario/<int:idProducto>')        
def get_comentario(idProducto):
        resp=srv_comentarios.get_comentarios(idProducto)
        json_items=[]
        content={}
        for resul in resp:
            content={'comentario_id':resul[0],'comprador':resul[1],'comentario':resul[2],'fecha':resul[3],'foto':resul[4],'usuario':resul[5],'respuesta':resul[6]}
            json_items.append(content)
            content={}
        return jsonify(json_items)



@app.route('/agregar_comentario',methods=['POST']) 
def agregar_comentario():
     _json=request.get_json(force=True)
     resp=srv_comentarios.set_comentario(_json)
     resp = jsonify('Comentarios Guardado.')
     resp.status_code = 200
     return resp

@app.route('/eliminar_comentario/<int:idComprador>/<int:idProducto>/<int:idComentario>',methods=['DELETE']) 
def eliminar_comentario(idComprador,idProducto,idComentario):
     resp=srv_comentarios.eliminar_comentario(idComprador,idProducto,idComentario)
     return resp