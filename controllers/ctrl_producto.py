import re
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
                            print(resp)
                            print(filename , " imagen cargada")
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

        print(resp)
    
        if resp == 'ok':
            response = jsonify("Producto eliminado con exito")                                                                                   #En la posicion 0 viene el estado en la 1 viene la lista de datos o el mensaje del error
            response.status_code = 200
            return response

        else:
            response = jsonify("No se puedo eliminar, intente de nuevo")
            response.status_code = 401 
        return response
 except Exception as ex:
        response = jsonify(repr("Hubo problemas internos"))
        response.status_code = 500
        return response 

@app.route('/update_product', methods=['POST'])  #esta en desarrpllo
def update_product():
 if request.method == 'POST':

       data = request.form['dataProducto']

       images_delete = request.form['imagenesEliminar']

       data_json = json.loads(data)
       images_delete_json = json.loads(images_delete)

       print(images_delete)

       srv_producto.delete_images_update(images_delete_json)

       resp_dir =  srv_direccion.update_direccion_producto(data_json)


       if resp_dir== 'ok':       
            res = srv_producto.update_product(data_json)


            if res == 'ok': 
                files = request.files.getlist('file') #    file = request.files['file']
                cont = 0

                for file in files:
                    try:
                        if file and allowed_file(file.filename):
                            pre_filename = str(round(time.time() * 1000)+cont) + '.' + file.filename.rsplit('.', 1)[1].lower()
                            filename = secure_filename(pre_filename)
                            file.save(os.getcwd() + '/resources/images/' + filename)
                            resp = srv_foto.save_photo(data_json['idProducto'], filename)
                            print(resp)
                            print(filename , " imagen cargada")
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
                    'publicacion':resul[5], 'prom_envio':resul[6], 'cost_envio':resul[7], 'oferta':resul[9], 'pais':resul[9], 'provincia':resul[10], 'canton':resul[11], 'categoria':resul[12], 'direccion_id':resul[13]}

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

@app.route('/get_calificacion_by_producto_id/<int:id>')
def get_calificacion_by_producto_id(id):
    try:
        resp = srv_producto.get_calificacion(id)
        print(resp)
        if(resp[0] == 'ok'):
            response = jsonify(resp[1])
            response.status_code = 200
            return response

        response = jsonify('No se pudo obtener la calificación')
        response.status_code = 401
        return response

    except Exception as ex:
        response = jsonify(repr(ex))
        response.status_code = 500
        return response 

@app.route('/get_deseos_id/<int:id>')
def get_deseos_by_id(id):
    try:
        resp = srv_producto.get_deseos(id)

        print(resp)
        if(resp[0] == 'ok'):
            json_items=[]
            content={}
            for resul in resp[1]:
                content={'id':resul[0],'nombre':resul[1], 'foto_url':resul[2]}
                json_items.append(content)
                content={}
            response = jsonify(json_items)
            response.status_code = 200
            return response
           
        response = jsonify('No se obtener los datos')
        response.status_code = 401
        return response

    except Exception as ex:
        response = jsonify(repr(ex))
        response.status_code = 500
        return response     


@app.route('/get_ofertas/<string:categoria>/<string:precioMenor>/<string:precioMayor>/<string:fechaInicio>/<string:fechaFinal>')
def get_ofertas(categoria, precioMenor, precioMayor, fechaInicio, fechaFinal):
 try:
       
        response = None

        categoria = getVarData(categoria)
        precioMenor = getVarData(precioMenor)
        precioMayor = getVarData(precioMayor)
        fechaInicio = getVarData(fechaInicio)
        fechaFinal = getVarData(fechaFinal)
        
        resp = srv_producto.get_ofertas(categoria,precioMenor, precioMayor, fechaInicio, fechaFinal)
        print(resp)
    
        if resp[0] == 'ok':
            rows = resp[1]
            content = {}    
            json_items = []
            for resul in rows:
                content = {'fecha_publicacion':resul[0],'nombre_producto':resul[1],'descripcion':resul[2], 'precio':resul[3],  'precio_oferta':resul[4], 'categoria':resul[5], 'tienda':resul[6]}

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

def getVarData(nombre):
    if(nombre == "none"):
        return None
    else:
        return nombre


def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/get_productosMasVendidos')
def get_productosMasVendidos():
     resp=srv_producto.get_productosMasVendidos()
     json_items=[]
     content={}
     for resul in resp:
            content={'producto_id':resul[0],'nombre':resul[1],'descripcion':resul[2],'precio':resul[3],'cantidad':resul[4],
                  'foto':resul[5],'vendidos':resul[6],'cost_envio':resul[7],'prom_envio':resul[8],'oferta':resul[9]}
            json_items.append(content)
            content={}
     return jsonify(json_items)