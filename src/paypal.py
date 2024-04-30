from flask import Flask, jsonify, Blueprint
import paypalrestsdk

app = Flask(__name__)

from db import Database
db = Database()

procesar_pago = Blueprint('procesar_pago', __name__)

paypalrestsdk.configure({
  "mode": "sandbox",  
  "client_id": "AWnSjr_p6ze5rf_SYbldhvGJY7cFz7DL1W8Te9sWo8vxDJ9pX4m9VYZhtJp-Yi1BlqnZUEV_xjVdyp9F",
  "client_secret": "ELN9gitr4tYKLSp2jxsigjSdkQIexyEhJmgCI2ihJLwRei9Kld7z8JswJjiglEW0r1Yqd5kCV-WNCIl9"
})

@procesar_pago.route('/procesar-pago', methods=['POST'])
def pago_paypal():
    payment = paypalrestsdk.Payment({
      "intent": "sale",
      "payer": {
        "payment_method": "paypal"
      },
      "redirect_urls": {
        "return_url": "http://127.0.0.1:5000/",
        "cancel_url": "http://127.0.0.1:5000/a"
      },
      "transactions": [{
        "item_list": {
          "items": [{
            "name": "Producto",
            "sku": "001",
            "price": "10.00",
            "currency": "USD",
            "quantity": 1
          }]
        },
        "amount": {
          "total": "10.00",
          "currency": "USD"
        },
        "description": "Descripción del producto"
      }]
    })

    if payment.create():
        return jsonify({"Compra realizada con exito": payment.id})
    else:
        return jsonify({"Error de compra": payment.error})

if __name__ == '__main__':
    app.run(debug=True)
