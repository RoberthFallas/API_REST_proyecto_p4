from flask import json, jsonify
from flask.json import request
from werkzeug.wrappers import response
from init import app
from services import svr_tienda
from services import srv_producto
from services import srv_comentarios
from services import srv_usuario
from services import srv_direccion
from controllers import ctrl_usuario


@app.route('/get_tiendas/')
def get_Tiendas():
    
        resp=svr_tienda.get_t()
        json_items=[]
        content={}
        for resul in resp:
            content={'tienda_id':resul[0],'descripcion':resul[1],'nombre':resul[2],'pais':resul[3],'provincia':resul[4],'canton':resul[5],'foto':resul[6]}
            json_items.append(content)
            content={}
        return jsonify(json_items)

@app.route('/get_categorias2/<int:id>')
def get_categorias2(id):
    
        resp=svr_tienda.get_categorias(id)
        json_items=[]
        content={}
        for resul in resp:
            content={'categoria_id':resul[0],'categoria':resul[1]}
            json_items.append(content)
            content={}
        return jsonify(json_items)
"""Obtiene un lista de tiendas de acuerdo a los filtros seleccionados, es decir, nombre y categoria"""
@app.route('/get_productosTiendas/<int:id>/<string:nombre>/<int:id_categoria>')
@app.route('/get_productosTiendas/<int:id>/<int:id_categoria>')
@app.route('/get_productosTiendas/<int:id>/<string:nombre>')
@app.route('/get_productosTiendas/<int:id>')
def get_productosTiendas(id,nombre=None,id_categoria=None):
    
        resp=svr_tienda.get_productosTiendas(id,nombre,id_categoria)
    
        json_items=[]
        content={}
        for resul in resp:
            califacion = srv_producto.get_calificacion(resul[0])[1]
            cant_lista_deseos = srv_producto.get_cant_deseos(resul[0])[1]
            print(califacion)
            content={'producto_id':resul[0],'precio':resul[1],'foto':resul[2],'nombre':resul[3], 'descripcion':resul[4], 'cantidad':resul[5], 
                    'publicacion':resul[6], 'prom_envio':resul[7], 'cost_envio':resul[8], 'oferta':resul[9], 'pais':resul[10], 'provincia':resul[11], 'canton':resul[12], 'calificacion':califacion, 'deseos':cant_lista_deseos}
            json_items.append(content)

            content={}
        return jsonify(json_items)

@app.route('/get_fotosProductos/<int:id>')        
def get_fotosProductos(id):
        resp=svr_tienda.get_fotosProductos(id)
        json_items=[]
        content={}
        for resul in resp:
            content={'foto_id':resul[0],'url':resul[1]}
            json_items.append(content)
            content={}
        return jsonify(json_items)

@app.route('/get_productoSelecionado/<int:id>')    
def get_productoSelecionado(id):
         resp=svr_tienda.get_productoSelecionado(id)
         json_items=[]
         content={}
         for resul in resp:
             calificacion = srv_producto.get_calificacion(resul[0])[1]
             content={'producto_id':resul[0],'precio':resul[1],'nombre':resul[2], 'descripcion':resul[3], 'cantidad':resul[4], 
                    'publicacion':resul[5], 'prom_envio':resul[6], 'cost_envio':resul[7], 'oferta':resul[8], 'pais':resul[9], 'provincia':resul[10], 'canton':resul[11], 'calificacion': calificacion}
             json_items.append(content)
             content={}
         return jsonify(json_items)
"""Subscripciones by id de tienda"""
@app.route('/get_subscripciones_by_id/<int:id>')
def get_subscripciones_by_id(id):
    try:
        resp = svr_tienda.get_subscripciones_by_id(id)

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


@app.route('/get_tienda_comentarios_no_leidos/<int:id>')        
def get_comentario(id):

    try: 
        resp=srv_comentarios.get_comentarios_tienda(id)
    
        json_items=[]
        content={}
        if(resp[0] == 'ok'):
            for resul in resp[1]:
                content={'comentario_id':resul[0],'comprador_id':resul[1],'producto_id':resul[2],'comentario':resul[3],'fecha':resul[4], 'foto':resul[5],'nombre_usuario':resul[6],'respuesta':resul[7], 'producto_nombre':resul[8], 'producto_foto':resul[9]}
                json_items.append(content)
                content={}
            return jsonify(json_items)
        
        response = jsonify('No se puede obtener los datos')
        response.status_code = 401
        return response

    except Exception as ex:
        response = jsonify(repr(ex))
        response.status_code = 500
        return response     


@app.route('/get_ventas_between/<int:id>/<string:startDate>/<string:endDate>')        
def get_ventas_between(startDate, endDate, id):

    try: 
        resp=svr_tienda.get_ventas_between(startDate, endDate, id)
    
        json_items=[]
        content={}
        if(resp[0] == 'ok'):
            for resul in resp[1]:
                content={'nombre':resul[0],'categoria':resul[1],'precio_estimado':resul[2],'precio_oferta':resul[3],'fecha_publicacion':resul[4], 'cantidad_vendida':resul[5],'total':resul[6]}
                json_items.append(content)
                content={}
            return jsonify(json_items)
        
        response = jsonify('No se puede obtener los datos')
        response.status_code = 401
        return response

    except Exception as ex:
        response = jsonify(repr(ex))
        response.status_code = 500
        return response     


        


@app.route('/get_tienda_data_by_user_id/<int:id>')  
def get_tienda_data_by_user_id(id):
    try:
        resp = svr_tienda.get_tienda_data_by_user_id(id)
        if resp[0] == "ok":
            _json = {"usuario_id": resp[1][0], "nombre_usuario":resp[1][1],
                    "usuario_email": resp[1][2], "usuario_foto":resp[1][3],
                    "usuario_telefono": resp[1][4], "usuario_cedula":resp[1][5],
                    "usuario_nombre_compl": resp[1][6], "usuario_tipo":resp[1][7],
                    "tienda_id": resp[1][8], "tienda_descripcion":resp[1][9],
                    "direccion_id": resp[1][10], "direccion_pais":resp[1][11],
                    "direccion_provincia": resp[1][12], "direccion_canton":resp[1][13]
                    }
            r = jsonify(_json)        
            return jsonify(_json)
        else:
            response = jsonify(resp[1])
            response.status_code = 204 if resp[0] == 'warn' else 500
            return response
    except Exception as ex:
        print(ex)

@app.route('/edit_tienda', methods=['PUT'])
def edit_tienda():
    try:
        str_data = request.form['string_data']
        _json = json.loads(str_data)
        
        if ctrl_usuario.check_update_data(_json['usuario_id'], _json['usuario_cedula'], _json['usuario_nom_usr']):
            user_srv_list = (_json['usuario_nom_usr'], _json['usuario_email'], 
                ctrl_usuario.update_profile_pictore(request.files.get('file'), _json['usuario_nom_usr'], _json['usuario_foto']),  
                _json['usuario_telefono'], _json['usuario_cedula'], _json['usuario_nombre_compl'], _json['usuario_id'])
            
            srv_usuario.update_user(user_srv_list)

            tienda_srv_list = (_json['tienda_descripcion'], _json['tienda_id'])
            svr_tienda.update_tienda(tienda_srv_list)

            direccion_srv_list = (_json['direccion_pais'], _json['direccion_provincia'], _json['direccion_canton'], _json['direccion_id'])
            srv_direccion.update_direccion(direccion_srv_list)
            
            if _json['usuario_contrasenna']:
                srv_usuario.change_password(_json['usuario_contrasenna'], _json['usuario_id'])
            return jsonify('Los datos de tu tienda han sido actualizados')
        else:
            response = jsonify("El nombre de usuario o cédula que has ingresado ya está en uso.")
            response.status_code = 409
            return response
    except Exception as ex:
        print(ex)




@app.route('/get_informacion_tienda/<int:id>')    
def get_informacion_tienda(id):
    try: 
        resp=svr_tienda.get_informacion_tienda(id)
        print(resp)
        if resp[0] == 'ok':
            _json={
                    'nombre':resp[1][0],'telefono':resp[1][1],'correo':resp[1][2],'descripcion':resp[1][3],'pais':resp[1][4],
                    'provincia':resp[1][5],'canton':resp[1][6]
                }
            return jsonify(_json)
        else:
            response = jsonify(resp[1])
            response.status_code = 204 if resp[0] == 'warn' else 500
            return response
    except Exception as ex:
        print(ex)
    

@app.route('/get_tiendas_by_param/<string:param>')
def get_tiendas_by_param(param):
    
        resp=svr_tienda.get_tiendas_by_param(param)
        if(resp[0] == "ok"):
            json_items=[]
            content={}
            for resul in resp[1]:
                content={'tienda_id':resul[0],'descripcion':resul[1],'nombre':resul[2],'pais':resul[3],'provincia':resul[4],'canton':resul[5],'foto':resul[6]}
                json_items.append(content)
                content={}
            return jsonify(json_items)


@app.route('/get_calificacion_by_tienda_id/<int:id>')
def get_calificacion_by_tienda_id(id):
    try:
        resp = svr_tienda.get_calificacion_tienda(id)
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
