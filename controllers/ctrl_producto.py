from flask import json, jsonify, request, flash, redirect, url_for
from init import app
from werkzeug.utils import secure_filename
from services import srv_producto
from services import srv_foto
from services import srv_direccion
import time

import os 


@app.route('/create_product', methods=['POST'])
def create_product():
   if request.method == 'POST':

       data = request.form['dataProducto']

       data_json = json.loads(data)

       resp_dir =  srv_direccion.insert_direccion_producto(data_json)
     

       if resp_dir[0] == 'ok':       
            res = srv_producto.create_product(data_json, resp_dir[1])

            print(res) 

            if res[0] == 'ok': 
                files = request.files.getlist('file') #    file = request.files['file']
                cont = 0
                for file in files:
                    try:
                        if file and allowed_file(file.filename):
                            pre_filename = str(round(time.time() * 1000)+cont) + '.' + file.filename.rsplit('.', 1)[1].lower()
                            filename = secure_filename(pre_filename)
                            file.save(os.getcwd() + '/resources/images/' + filename)
                            resp = srv_foto.save_photo(res[1], filename)
                            cont = cont + 1  
                    except FileNotFoundError:
                            respuesta = jsonify( "Hubo un error al guardar las imagenes del producto")
                            respuesta.status_code = 200
                            return respuesta
                           
                
                         
                respuesta = jsonify( "El producto se guardó exitosamente")
                respuesta.status_code = 200
                return respuesta
                
       respuesta = jsonify( "Surgieron problemas al guardar el producto. Contacte el administrador")
       respuesta.status_code = 500 
       return respuesta
  
@app.route('/delete_product/<string:id>', methods=['DELETE'])
def delele_product(id):
 try:
        response = None
        resp = srv_producto.delete_producto(id)
    
        if resp == 'ok':
            response = jsonify("Producto eliminado con exito")                                                                                   #En la posicion 0 viene el estado en la 1 viene la lista de datos o el mensaje del error
            response.status_code = 200
            return response

        else:
            response = jsonify(resp)
            response.status_code = 401 
        return response
 except Exception as ex:
        response = jsonify(repr(ex))
        response.status_code = 500
        return response 

@app.route('/update_product/', methods=['PUT'])
def update_product():
 try:
        response = None
        _json = request.get_json(force=True)
        resp = srv_producto.delete_producto(id)
    
        if resp == 'ok':
            response = jsonify("Producto eliminado con exito")                                                                                   #En la posicion 0 viene el estado en la 1 viene la lista de datos o el mensaje del error
            response.status_code = 200
            return response

        else:
            response = jsonify(resp)
            response.status_code = 401 
        return response
 except Exception as ex:
        response = jsonify(repr(ex))
        response.status_code = 500
        return response 


@app.route('/get_product_by_id/<int:id>')
def get_product_by_id(id):
 try:
        print("ddentro de get by id")
        response = None
        
        resp = srv_producto.get_product_by_id(id)
        print(resp)
    
        if resp[0] == 'ok':
            rows = resp[1]
            content = {}    
            json_items = []
            for resul in rows:
                content = {'producto_id':resul[0],'precio':resul[1],'nombre':resul[2], 'descripcion':resul[3], 'cantidad':resul[4], 
                    'publicacion':resul[5], 'prom_envio':resul[6], 'cost_envio':resul[7], 'oferta':resul[9], 'pais':resul[9], 'provincia':resul[10], 'canton':resul[11]}

                json_items.append(content)
                content = {}

            response = jsonify(json_items)
            response.status_code = 200
            return(response)
        else:
            response = jsonify(resp[0])
            response.status_code = 401 if resp[0] == 'warn' else 500
            return(response)
    
     
 except Exception as ex:
        response = jsonify(repr(ex))
        response.status_code = 500
        return response 




        
def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


