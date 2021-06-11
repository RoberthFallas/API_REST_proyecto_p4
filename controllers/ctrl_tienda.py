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

@app.route('/get_categorias/<int:id>')
def get_categorias(id):
    
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
            content={'producto_id':resul[0],'precio':resul[1],'foto':resul[2],'nombre':resul[3]}
            json_items.append(content)
            content={}
        return jsonify(json_items)