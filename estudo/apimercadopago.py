# def gerar_link_pagamento():
#     import mercadopago

#     sdk = mercadopago.SDK("APP_USR-3882407833501659-042310-a54520d8d9539beb21ddabf7163c5dbb-2404911566")

#     request_options = mercadopago.config.RequestOptions()
#     request_options.custom_headers = {
#         'x-idempotency-key': '<SOME_UNIQUE_VALUE>'
#     }

#     payment_data = {
#         "items": [
#             {
#                 "id": "1234",
#                 "title": "Camisa do Atlético-MG",
#                 "quantity": 1,
#                 "currency_id": "BRL",
#                 "unit_price": 299.99,
#             }
#         ],
#             #Validação do retorno (webhooks) fazer depois
#             # O ideal é usar webhooks (notificações automáticas) para confirmar pagamentos com mais segurança, ao invés de confiar apenas no redirecionamento (back_urls).
#             # Isso permite que você confirme se o pagamento foi realmente aprovado no servidor.
#         "back_urls": {
#             "success": "https://0316-2804-540-153-2d00-701b-6a3c-7ad9-891f.ngrok-free.app/compracerta",
#             "failure": "https://0316-2804-540-153-2d00-701b-6a3c-7ad9-891f.ngrok-free.app/compraerrada",
#             "pending": "https://0316-2804-540-153-2d00-701b-6a3c-7ad9-891f.ngrok-free.app/compraerrada"
#         },
#         "auto_return": "approved"
#     }

#     result = sdk.preference().create(payment_data, request_options)
#     payment = result["response"]
#     print("Resposta da API Mercado Pago:", result)
#     return payment["init_point"]


# #Nunca envie seu access token para o navegador.
# #Use o init_point para redirecionar o cliente ao checkout com segurança 

# # No terminal, rode o Flask app:
# # python app.py

# # Em outro terminal, rode o ngrok:
# # ngrok http 5000

# # se aparecer isto no cmd  authentication failed: Usage of ngrok requires a verified account and authtoken.
# # Perfeito, isso significa que o ngrok foi instalado corretamente, mas você precisa autenticar sua conta com um token antes de usá-lo. Isso é obrigatório a partir das versões mais recentes do ngrok.
# # Crie uma conta gratuita (no ngrok), pegue seu authtoken Copie e cole esse comando no seu terminal.

# # ngrok start default

# # Isso que apareceu é uma tela de aviso de segurança padrão do ngrok, chamada de "ngrok inspect page". Ela aparece quando você tenta acessar diretamente uma URL do ngrok via redirecionamento automático, como o Mercado Pago faz com auto_return.

# # ngrok http --host-header=rewrite 5000


# # Copie a URL gerada pelo ngrok (ex: https://xxxxx.ngrok-free.app) e use essa nos seus back_urls na API do Mercado Pago.


# # ngrok config edit
# #para editar e executar o passo logo abaixo

# # caso de um erro na url de direcionamento, indica que o seu arquivo ngrok.yml tem erro de formatação (espaçamento ou estrutura incorreta). YAML é sensível à indentação — qualquer espaço errado gera erro.
# # version: "2"
# # authtoken: 2wUeLAazjzZYpjlNNRLqKT4the3_4ur8nm3yqd5geiNCDrmSx
# # tunnels:
# #   default:
# #     proto: http
# #     addr: 5000
# #     host_header: rewrite

