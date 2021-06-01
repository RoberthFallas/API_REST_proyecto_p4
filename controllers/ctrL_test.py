from flask.json import jsonify
from init import app
from services import tests



@app.route('/test_database_connection')
def test_database_connection():
    try:
        return jsonify(tests.test_database_conection())
    except Exception as ex:
        print(ex)
