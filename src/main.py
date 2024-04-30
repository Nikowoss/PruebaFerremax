from flask import Flask
from Venta import insertar
from Producto import consultar_producto
from paypal import procesar_pago

app = Flask(__name__)

app.register_blueprint(insertar)
app.register_blueprint(consultar_producto)
app.register_blueprint(procesar_pago)

if __name__ == "__main__":
    app.run(debug=True)
