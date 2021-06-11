from flask import json, jsonify, request, flash, redirect, url_for
from init import app
from werkzeug.utils import secure_filename
from services import srv_producto
from services import srv_foto
from services import srv_direccion

import os 



@app.route('/create_producto', methods=['POST'])
def create_producto():
   if request.method == 'POST':
        # check if the post request has the file part
        if 'imagen' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['imagen']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print(os.path.join(app.config['UPLOAD_FOLDER']))
            file.save(os.getcwd() + '/resources/images/' + filename)
            return 'success'



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
                for file in files:
                    try:
                        if file and allowed_file(file.filename):
                            filename = secure_filename(file.filename)
                            file.save(os.getcwd() + '/resources/images/' + filename)
                            resp = srv_foto.save_photo(res[1], filename)
                            print(resp[1])      
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
  

    
        
def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS