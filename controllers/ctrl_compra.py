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

@app.route('/get_comprar/<int:idCliente>/<int:idFormaPago>')
def get_comprar(idCliente,idFormaPago):
    resp=srv_compra.getCantidadProducto(idCliente)
    cantidadExiste=True
    if resp!='error':   
        for resul in resp:
            if resul[0]>resul[1]:
               cantidadExiste=False
    if(cantidadExiste==True):
        montoTotal=0
        for costos in resp:
            montoTotal=montoTotal+costos[0]*costos[2]
        formPago=srv_compra.getFormaPagoSeleccionada(idCliente,idFormaPago)
        aux=0
        for formPag in formPago:
            aux=formPag[0]
        if(aux>montoTotal):               
          resp = jsonify('Comentarios Guardado.'+montoTotal)
          resp.status_code = 200
          return resp
        else:
            resp = jsonify('Comentarios Guardado.'+montoTotal)
            resp.status_code = 200
            return resp 
    else:
       resp = jsonify('Error.')
       resp.status_code = 200
       return resp