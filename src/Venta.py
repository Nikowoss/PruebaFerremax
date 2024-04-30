from flask import Flask, request, jsonify, Blueprint
import mysql.connector

app = Flask(__name__)

# Configuración de la conexión a la base de datos
db_connection = mysql.connector.connect(
    host='localhost',
    port='3306',
    user='root',
    password='',
    db='ferremax'
)

insertar = Blueprint('insertar', __name__)

@insertar.route('/insertar-ventas', methods=['POST'])
def venta():
    # Obtener los datos enviados en la solicitud
    datos = request.json

    # Extraer los valores de los campos
    campo1 = datos.get('campo1')
    campo2 = datos.get('campo2')

    try:
        cursor = db_connection.cursor()

        # Ejecutar la consulta INSERT
        cursor.execute("INSERT INTO cliente (rut, nombre) VALUES (%s, %s)", (campo1, campo2))
        db_connection.commit()

        cursor.close()

        # Devolver una respuesta exitosa en formato JSON
        respuesta = {'mensaje': 'Los datos se insertaron correctamente'}
        return jsonify(respuesta), 200
    except Exception as e:
        # Devolver un mensaje de error en caso de fallo
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
