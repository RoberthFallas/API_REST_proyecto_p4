from flask import json, jsonify, request, flash, redirect, url_for 
from init import app 
from werkzeug.utils import secure_filename 
from services import srv_ruleta  
 
@app.route('/create_giro_ruleta', methods=['POST']) 
def create_giro_ruleta(): 
    try: 
        _json = request.get_json(force=True) 
        resp = srv_ruleta.create_giro_ruleta(_json) 
        print(resp) 
        if resp is 'ok': 
           return jsonify("Forma de pago guardada") 
        else: 
            response = jsonify(resp[1]) 
            response.status_code = 409 
            return response 
    except Exception as ex: 
        print(ex) 
 
 
@app.route('/get_total_giros_hoy/<int:id>') 
def get_total_giros_hoy(id): 
 try:   
        response = None 
        resp = srv_ruleta.get_giros_hoy(id) 
        print(resp) 
     
        if resp[0] == 'ok': 
            response = jsonify(resp[1][0][0]) 
            response.status_code = 200 
            return(response) 
        else: 
            response = jsonify("Hubo problemas obteniendo los datos") 
            response.status_code = 401  
            return(response) 
 except Exception as ex: 
        response = jsonify(repr(ex)) 
        response.status_code = 500 
        return response

