from flask import json, jsonify
from werkzeug.wrappers import response
from init import app
from services import svr_tienda
from services import srv_producto
from services import srv_comentarios


@app.route('/get_tiendas/')
def get_Tiendas():
    
        resp=svr_tienda.get_t()
        json_items=[]
        content={}
        for resul in resp:
            content={'tienda_id':resul[0],'descripcion':resul[1],'nombre':resul[2],'pais':resul[3],'provincia':resul[4],'canton':resul[5]}
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
             content={'producto_id':resul[0],'precio':resul[1],'nombre':resul[2], 'descripcion':resul[3], 'cantidad':resul[4], 
                    'publicacion':resul[5], 'prom_envio':resul[6], 'cost_envio':resul[7], 'oferta':resul[8], 'pais':resul[9], 'provincia':resul[10], 'canton':resul[11]}
             json_items.append(content)
             content={}
         return jsonify(json_items)

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
                content={'nombre':resul[0],'categoria':resul[1],'precio_estimado':resul[2],'precio_oferta':resul[3],'fecha':resul[4], 'cantidad_vendida':resul[5],'total':resul[6]}
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


        

