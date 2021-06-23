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