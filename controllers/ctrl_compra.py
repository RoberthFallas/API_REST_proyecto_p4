from flask import json, jsonify, request, flash, redirect, url_for
from init import app
from werkzeug.utils import secure_filename
from services import srv_compra

@app.route('/get_formaPago/<int:idCliente>')        
def get_formaPago(idCliente):
        resp=srv_compra.get_formaPagoCliente(idCliente)
        json_items=[]
        content={}
        for resul in resp:
            content={'formaPago_id':resul[0],'numeroTarjeta':resul[1]}
            json_items.append(content)
            content={}
        return jsonify(json_items)

@app.route('/get_DirrecionEnvio/<int:idCliente>')        
def get_DirrecionEnvio(idCliente):
        resp=srv_compra.get_DirrecionEnvio(idCliente)
        json_items=[]
        content={}
        for resul in resp:
            content={'envio_id':resul[0],'pais':resul[1],'provincia':resul[2],'canton':resul[3],'casillero':resul[4]}
            json_items.append(content)
            content={}
        return jsonify(json_items)