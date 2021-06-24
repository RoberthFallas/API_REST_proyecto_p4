from flask import json, jsonify, request, flash, redirect, url_for
from init import app
from werkzeug.utils import secure_filename
from services import srv_reporteAbuso


@app.route('/agregar_reporte',methods=['POST']) 
def agregar_reporte():
     _json=request.get_json(force=True)
     resp=srv_reporteAbuso.insertar_reporte(_json)
     resp = jsonify('Guardada.')
     resp.status_code = 200
     return resp

'Se puede hacer un reporte si existe una factura con un producto de la tienda'
@app.route('/get_reporteFactura/<int:idCliente>/<int:idTienda>')        
def get_reporteFactura(idCliente,idTienda):
  try:
        resp=srv_reporteAbuso.get_comprasReporte(idCliente,idTienda)
        if resp[0] == 'ok':
            _json={
                'cantidad':resp[1][0]
                }
            return jsonify(_json)
        else:
            response = jsonify(resp[1])
            response.status_code = 204 if resp[0] == 'warn' else 500
            return response
  except Exception as ex:
        print(ex)
        
@app.route('/get_reportesRealizados/<int:idCliente>/<int:idTienda>')        
def get_reportesRealizados(idCliente,idTienda):
  try:
        resp=srv_reporteAbuso.get_reportesRealizados(idCliente,idTienda)
        if resp[0] == 'ok':
            _json={
                'cantidad':resp[1][0]
                }
            return jsonify(_json)
        else:
            response = jsonify(resp[1])
            response.status_code = 204 if resp[0] == 'warn' else 500
            return response
  except Exception as ex:
        print(ex)        

@app.route('/eliminar_reporte/<int:idComprador>/<int:idTienda>',methods=['DELETE']) 
def eliminar_reporte(idComprador,idTienda):
     resp=srv_reporteAbuso.eliminar_reporte(idComprador,idTienda)
     return resp