from flask import json, jsonify, request, flash, redirect, url_for
from init import app
from werkzeug.utils import secure_filename
from services import srv_compra
from services import srv_carrito
from services import srv_producto

@app.route('/get_formaPago/<int:idCliente>')        
def get_formaPago(idCliente):
        resp=srv_compra.get_formaPagoCliente(idCliente)
        json_items=[]
        content={}
        for resul in resp:
            content={'formaPago_id':resul[0],'numeroTarjeta':resul[1]}
            json_items.append(content)
            content={}
        return jsonify(json_items)

@app.route('/get_DirrecionEnvio/<int:idCliente>')        
def get_DirrecionEnvio(idCliente):
        resp=srv_compra.get_DirrecionEnvio(idCliente)
        json_items=[]
        content={}
        for resul in resp:
            content={'envio_id':resul[0],'pais':resul[1],'provincia':resul[2],'canton':resul[3],'casillero':resul[4]}
            json_items.append(content)
            content={}
        return jsonify(json_items)

@app.route('/get_comprar/<int:idCliente>/<int:idFormaPago>/<string:cvv>/<int:idDirrecion>')
def get_comprar(idCliente,idFormaPago,cvv,idDirrecion):
    'Consultar si existe la cantidad solicitada del producto'
    resp=srv_compra.getCantidadProducto(idCliente)
    cantidadExiste=True
    if resp!='error':   
        'Revisar la cantidad de los productos'
        for resul in resp:
            if resul[0]>resul[1]:
               cantidadExiste=False
    if(cantidadExiste==True):
        subTotal=0
        costoEnvio=0
        'Calcular costos'
        for costos in resp:
            if(costos[3]>0):
                subTotal=subTotal+costos[0]*costos[3]
                costoEnvio=costoEnvio+costos[4]
            else:
                subTotal=subTotal+costos[0]*costos[2]
                costoEnvio=costoEnvio+costos[4]
        'Consultar si la forma de pago tiene el monto para pagar'
        formPago=srv_compra.getFormaPagoSeleccionada(idFormaPago)
        if formPago[0]=='ok':
            if(formPago[1][1]==cvv):
                if(formPago[1][0]>subTotal+costoEnvio):               
                    factura=srv_compra.insertarFactura(idCliente,idFormaPago,subTotal,subTotal+costoEnvio,idDirrecion)
                    for detalle in resp:
                        if(detalle[3]>0):
                            costo=detalle[0]*detalle[3]
                            srv_compra.agregarDetalle(detalle[5],factura[1],detalle[0],costo)
                            srv_carrito.eliminar_carrito(idCliente,detalle[5])
                            srv_producto.update_product_cantidad(detalle[1]-detalle[0],detalle[5])
                        else:
                            costo=detalle[0]*detalle[2]
                            srv_compra.agregarDetalle(resul[5],factura[1],detalle[0],costo)
                            srv_carrito.eliminar_carrito(idCliente,detalle[5])
                            srv_producto.update_product_cantidad(detalle[1]-detalle[0],detalle[5])
                    resp = jsonify('Compra correcta')
                    resp.status_code = 200
                    return resp  
                else:
                        resp = jsonify('La compra sobrepasa el monto')
                        resp.status_code = 200
                        return resp  
            else:
                 resp = jsonify('El cvv no concuerda')
                 resp.status_code = 200
                 return resp          
        else:
            resp = jsonify('Error forma de pago mala')
            resp.status_code = 200
            return resp 
    else:
       resp = jsonify('Error cantida producto.')
       resp.status_code = 200
       return resp

