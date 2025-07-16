from flask import Flask
# from dotenv import load_dotenv
# pip install flask-login flask-bcrypt
# from flask_login import LoginManager
# inicio da nosso controle de login.
# pip install flask-login flask-bcrypt 
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
# responsavel por busca os valores
import os
# load_dotenv('.env')

#vamos começa a configura o nosso banco de dados
#pip install Flask-SQLAlchemy Flask-Migrate
#depois temos de import antes de app
# 

# vamos deixa nosso nossas chaves mais seguras utilizando variaveis de ambiente
# pip install python-dotenv


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

login_manager=LoginManager(app)
bcrypt=Bcrypt(app)
# controle de login
login_manager.login_view='login'


# importa as rotas
from estudo.routes import homepage

