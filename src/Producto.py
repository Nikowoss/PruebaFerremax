from flask import Flask, jsonify,Blueprint
import mysql.connector

app = Flask(__name__)

from db import Database
db = Database()

consultar_producto = Blueprint('consultar_producto', __name__)


@consultar_producto.route('/consultar-producto', methods=['GET'])
def productos():
    connection = db.get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM producto")
    resultados = cursor.fetchall()
    columnas = [column[0] for column in cursor.description]
    datos = []
    for fila in resultados:
        datos.append(dict(zip(columnas, fila)))
    cursor.close()
    connection.close()
    return jsonify(datos)

@app.route('/producto', methods=['GET'])
def obtener_producto():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='',
            db='ferremax'
        )
        if connection.is_connected():
            print("Conectado")
            
    except mysql.connector.Error as ex:
        return jsonify({'error': str(ex)})

if __name__ == '__main__':
    app.run(debug=True)
