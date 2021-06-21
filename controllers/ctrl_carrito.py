from flask import json, jsonify, request, flash, redirect, url_for
from init import app
from werkzeug.utils import secure_filename
from services import srv_carrito

@app.route('/get_miCarrito/<int:idCliente>')        
def get_miCarrito(idCliente):
        resp=srv_carrito.get_misDeseos(idCliente)
        json_items=[]
        content={}
        for resul in resp:
            content={'producto':resul[0],'nombre':resul[1],'descripcion':resul[2],'foto':resul[3],'cantidad':resul[4]}
            json_items.append(content)
            content={}
        return jsonify(json_items)