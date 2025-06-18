from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import mercadopago

app = Flask(__name__)
CORS(app)

sdk = mercadopago.SDK("APP_USR-3882407833501659-042310-a54520d8d9539beb21ddabf7163c5dbb-2404911566")  # Substitua pelo seu access token do Mercado Pago

@app.route("/criar_pagamento", methods=["POST", "OPTIONS"])
def criar_pagamento():
    # Lida com preflight (OPTIONS)
    if request.method == "OPTIONS":
        response = make_response()
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Headers", "Content-Type")
        response.headers.add("Access-Control-Allow-Methods", "POST, OPTIONS")
        return response, 200

    # Requisição real (POST)
    dados = request.get_json()
    titulo = dados.get("titulo")
    preco = float(dados.get("preco"))

    preference_data = {
        "items": [
            {
                "title": titulo,
                "quantity": 1,
                "currency_id": "BRL",
                "unit_price": preco
            }
        ]
    }

    preference_response = sdk.preference().create(preference_data)
    init_point = preference_response["response"]["init_point"]

    response = jsonify({"init_point": init_point})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == "__main__":
    app.run(port=5000, debug=True)


# Implemente Webhooks (opcional, mas recomendado)
# Se quiser saber com certeza quando um pagamento foi aprovado, recusado ou pendente, use webhooks. O Mercado Pago envia notificações automáticas para uma URL do seu backend sempre que o status muda.
# Em outro terminal, rode o ngrok:
# ngrok http 5000
# ngrok start default
