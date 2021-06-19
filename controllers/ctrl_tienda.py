from flask import json, jsonify
from werkzeug.wrappers import response
from init import app
from services import svr_tienda

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
            content={'producto_id':resul[0],'precio':resul[1],'foto':resul[2],'nombre':resul[3], 'descripcion':resul[4], 'cantidad':resul[5], 
                    'publicacion':resul[6], 'prom_envio':resul[7], 'cost_envio':resul[8], 'oferta':resul[9], 'pais':resul[10], 'provincia':resul[11], 'canton':resul[12]}
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


@app.route('/get_tienda_data_by_user_id/<int:id>')  
def get_tienda_data_by_user_id(id):
    try:
        resp = svr_tienda.get_tienda_data_by_user_id(id)
        if resp[0] is "ok":
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

