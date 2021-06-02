from flask.json import jsonify
from init import app
from services import srv_tests



@app.route('/test_database_connection')
def test_database_connection():
    try:
        return jsonify(srv_tests.test_database_conection())
    except Exception as ex:
        print(ex)



@app.route('/test_pasword_encript/<string:passw>')
def test_pasword_encript(passw):
    try:
        resp = srv_tests.test_pasword_encript(passw)
        if(resp[0] == 'ok'):
            return jsonify('Registro guardado de manera exitosa')
        else:
            return jsonify('Ha ocurrido un error: ' + resp[1])
    except Exception as ex:
        print(ex)



@app.route('/test_password_match/<int:id>/<string:passw>')
def test_password_match(id, passw):
    try:
        resp = srv_tests.test_password_match(id, passw)
        if(resp[0] == 'ok'):
            return jsonify('Contrasena ha hecho match')
        else:
            return jsonify('Ha ocurrido un error: ' + resp[1])
    except Exception as ex:
        print(ex)
