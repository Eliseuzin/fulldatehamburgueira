from flask import Flask
# from flask_login import LoginManager
from flask_bcrypt import Bcrypt

# ✅ Causa prováveis de erros:
# O problema não é no seu projeto, nem no código, mas sim porque o Python que está rodando o script não é o mesmo Python que tem o Flask-Login instalado.

# Apesar de o terminal mostrar (venv) ativado, o VS Code ou o terminal pode estar rodando o Python global (fora do venv).
# where python
# Se estiver certo, o primeiro caminho listado deve ser algo como:
# E:\bettersites\finishedhamburgeria\fulldatehamburgueira\venv\Scripts\python.exe

# Se estiver listando algo como:
# C:\Users\vin1z\AppData\...
# então você está rodando o Python errado, e o flask_login não está instalado lá.

# 💡 É o equivalente a dizer:
# "Ei, instale esse pacote exatamente neste projeto aqui, não importa o resto do sistema!"

# .\venv\Scripts\pip.exe install flask-bcrypt


#instartar nosso aplicativo
app=Flask(__name__)

# controle de login
# login_manager=LoginManager(app)
# login_manager.login_view='login'
# bcrypt=Bcrypt(app)



from estudo import routes  # importa as rotas

