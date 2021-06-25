from flask import json, jsonify, request, flash, redirect, url_for
from init import app
from werkzeug.utils import secure_filename
from services import srv_facturas

@app.route('/get_factura/<int:id>')        
def get_factura(id):
    try:
        resp= srv_facturas.get_factura_by_id(id)
        json_items=[]
        content={}
        content_ft = {}

        print(resp)

        if(resp[0] == "ok"):
            resul = resp[1]

            resp_detalles = srv_facturas.get_factura_detalles_by_id(id)
            print(resp_detalles[1])
            for resul_detalles in resp_detalles[1]:
                content={'nombre_producto':resul_detalles[0],'cantidad':resul_detalles[1], 'precio_unitario':resul_detalles[2], 'total':resul_detalles[3],  'tienda':resul_detalles[4],  'costo_envio':resul_detalles[5] } 
                json_items.append(content)
                content={}

            print(json_items)
            tarjeta = (resul[10][:-4] + "XXXX")   
            content_ft={'nombre_cliente':resul[0],'cedula':resul[1], 'email':resul[2],'telefono':resul[3], 'pais':resul[4],
                        'provincia':resul[5], 'canton':resul[6],'codigo_postal':resul[7], 'casillero':resul[8],'observaciones':resul[9], "tarjeta":tarjeta, "regalia":[11], "subtotal":resul[12], "total": resul[13], "detalles": json_items }
                
            response = jsonify(content_ft)
            response.status_code = 200
            return  response

        return jsonify("No se pudieron obtener los datos")
        
    except Exception as ex:
        response = jsonify(repr(ex))
        response.status_code = 500
        return response 
        
        


