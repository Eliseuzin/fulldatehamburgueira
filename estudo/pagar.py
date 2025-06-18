# # Esse erro é causado por CORS (Cross-Origin Resource Sharing) — ou seja, seu navegador está bloqueando a requisição porque o HTML está sendo servido de http://127.0.0.1:5501, mas a API está em https://...ngrok-free.app.

# #pip install flask-cors
# #para roda o cors e da seguimento ao pagamento

# #////
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import mercadopago

# app = Flask(__name__)
# #////
# # Configuração robusta de CORS
# #  isso aqui ativa o CORS para todas as origens
#  #Isso permite chamadas de qualquer origem (você pode restringir se quiser)
# # CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

# # sdk = mercadopago.SDK("APP_USR-3882407833501659-042310-a54520d8d9539beb21ddabf7163c5dbb-2404911566")

# # @app.route("/criar_pagamento", methods=["POST", "OPTIONS"])
# # def criar_pagamento():
# #     if request.method == "OPTIONS":
# #         # Resposta para o preflight
# #         response = app.make_default_options_response()
# #         response.headers.add("Access-Control-Allow-Origin", "*")
# #         response.headers.add("Access-Control-Allow-Headers", "Content-Type")
# #         response.headers.add("Access-Control-Allow-Methods", "POST, OPTIONS")
# #         return response

# #     # POST real (criação do pagamento)
# #     dados = request.get_json()
# #     titulo = dados.get("titulo")
# #     preco = float(dados.get("preco"))

# #     preference_data = {
# #         "items": [
# #             {
# #                 "title": titulo,
# #                 "quantity": 1,
# #                 "currency_id": "BRL",
# #                 "unit_price": preco
# #             }
# #         ]
# #     }

# #     preference_response = sdk.preference().create(preference_data)
# #     init_point = preference_response["response"]["init_point"]

# #     response = jsonify({"init_point": init_point})
# #     response.headers.add("Access-Control-Allow-Origin", "*")
# #     return response

# # if __name__ == "__main__":
# #     app.run(debug=True)
# #////
# from flask import Flask, request, jsonify, make_response
# from flask_cors import CORS
# import mercadopago

# app = Flask(__name__)
# CORS(app)  # Isso ativa o CORS globalmente

# sdk = mercadopago.SDK("SEU_ACCESS_TOKEN")

# @app.route("/criar_pagamento", methods=["POST", "OPTIONS"])
# def criar_pagamento():
#     # Resposta ao preflight (OPTIONS)
#     if request.method == "OPTIONS":
#         response = make_response()
#         response.headers.add("Access-Control-Allow-Origin", "*")
#         response.headers.add("Access-Control-Allow-Headers", "Content-Type")
#         response.headers.add("Access-Control-Allow-Methods", "POST, OPTIONS")
#         return response, 200

#     # Requisição POST real
#     dados = request.get_json()
#     titulo = dados.get("titulo")
#     preco = float(dados.get("preco"))

#     preference_data = {
#         "items": [
#             {
#                 "title": titulo,
#                 "quantity": 1,
#                 "currency_id": "BRL",
#                 "unit_price": preco
#             }
#         ]
#     }

#     preference_response = sdk.preference().create(preference_data)
#     init_point = preference_response["response"]["init_point"]

#     response = jsonify({"init_point": init_point})
#     response.headers.add("Access-Control-Allow-Origin", "*")
#     return response
# #////