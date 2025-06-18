# # #pip install Flask and pip install mercadopago no cmd
# # #arquivo não poder conter o nome como flask,pois, quando for import ira da erro
# # from flask import Flask, render_template
# # from apimercadopago import gerar_link_pagamento


# from flask import Flask, render_template
# from apimercadopago import gerar_link_pagamento  # Verifique o nome!

# # #para roda o cors e da seguimento ao pagamento
# # from flask import Flask, request, jsonify
# # from flask_cors import CORS
# # import mercadopago

# app = Flask(__name__)

# @app.route("/")
# def home():
#     link_pagamento = gerar_link_pagamento()
#     return render_template("home.html", link_pagamento=link_pagamento)

# @app.route("/compracerta")
# def compra_certa():
#     return render_template("compracerta.html")

# @app.route("/compraerrada")
# def compra_errada():
#     return render_template("compraerrada.html")

# if __name__ == "__main__":
#     app.run(debug=True)

# #fazer cadastro no ngrok e configurar o restante do codigo do mercado pago


