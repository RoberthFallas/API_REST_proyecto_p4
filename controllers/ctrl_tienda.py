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
            content={'categoria':resul[0]}
            json_items.append(content)
            content={}
        return jsonify(json_items)