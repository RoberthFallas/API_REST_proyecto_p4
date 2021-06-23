from flask import json, jsonify
from werkzeug.wrappers import response
from init import app
from services import srv_compradores


@app.route('/get_compras_between/<int:id>/<string:startDate>/<string:endDate>')        
def get_compras_between(id, startDate, endDate):

    try: 
        resp= srv_compradores.get_compras_between (id, startDate, endDate)
        print(resp)
    
        json_items=[]
        content={}
        if(resp[0] == 'ok'):
            for resul in resp[1]:
                tarjeta = (resul[9][:-4] + "XXXX")   
                content={'nombre_usuario':resul[0],'nombre_producto':resul[1],'descripcion_producto':resul[2],'categoria':resul[3],'precio':resul[4],'cantidad_comprada':resul[5],  'precio_total':resul[6],'factura_id':resul[7],'precio_final':resul[8],'tarjeta':tarjeta }
                json_items.append(content)
                content={}
            return jsonify(json_items)
        
        response = jsonify('No se puede obtener los datos')
        response.status_code = 401
        return response

    except Exception as ex:
        response = jsonify(repr(ex))
        response.status_code = 500
        print(response)
        return response     

@app.route('/get_productos_mas_dinero/<int:id>/<string:startDate>/<string:endDate>')        
def get_productos_mas_dinero(id, startDate, endDate):

    try: 
        resp= srv_compradores.get_productos_mas_dinero(id, startDate, endDate)
        print(resp)
    
        json_items=[]
        content={}
        if(resp[0] == 'ok'):
            for resul in resp[1]:
                content={'nombre_producto':resul[0],'cantidad':resul[1], 'total':resul[2] }
                json_items.append(content)
                content={}
            return jsonify(json_items)
        
        response = jsonify('No se puede obtener los datos')
        response.status_code = 401
        return response

    except Exception as ex:
        response = jsonify(repr(ex))
        response.status_code = 500
        print(response)
        return response  

@app.route('/get_susbcripciones_deseos/<int:id_comprador>')        
def get_susbcripciones_deseos(id_comprador):

    try: 
        subs= srv_compradores.get_subscripciones(id_comprador)
        print(subs)
    
        json_items=[]
        content={}
        if(subs[0] == 'ok'):
            for resul in subs[1]:
                json_deseos = []
                content_deseos = {}
                deseos = srv_compradores.get_deseos_by_tienda(id_comprador, resul[0])
                for deseo in deseos[1]:
                    content_deseos = {'nombre_producto':deseo[0],'precio_producto':deseo[1]}
                    json_deseos.append(content_deseos)

                print(json_deseos)
                content={'id_tienda':resul[0],'nombre_tienda':resul[1], 'productos_deseados':json_deseos }
                
                json_items.append(content)
                content={}
               
            
            return jsonify(json_items)
        
        response = jsonify('No se puede obtener los datos')
        response.status_code = 401
        return response

    except Exception as ex:
        response = jsonify(repr(ex))
        response.status_code = 500
        print(response)
        return response     
