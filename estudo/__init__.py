from flask import Flask
#vamos começa a configura o nosso banco de dados
#pip install Flask-SQLAlchemy Flask-Migrate
#depois temos de import antes de app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# vamos deixa nosso nossas chaves mais seguras utilizando variaveis de ambiente
# pip install python-dotenv
from dotenv import load_dotenv
# inicio da nosso controle de login.
# pip install flask-login flask-bcrypt
# from flask_login import LoginManager
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

# responsavel por busca os valores
import os
load_dotenv('.env')


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

#configurar o banco de dados
#quando criamos o banco de dados, ele chamará database.db
# app.config['SQLALCHEMY_DATABASE_URI']=os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'
#aumenta a prioridade, e evita o checking
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
#mais para frente aprenderemos a deixa o nosso banco de dados mais seguro, sem deixa chaves de acesso livres
# app.config['SECRET_KEY']=os.getenv('SECRET_KEY')
app.config['SECRET_KEY']='8a97b281fcaf00eaee650eb9078eded3d3c0656406f7d8b103191d1fb7f3ef18598a55ae52791310f2e96b716d17c78de9e1'
db=SQLAlchemy(app)
migrate=Migrate(app, db)
#comando para criar o banco de dados
#flask db init
#é necessário apenas um banco de dados por projeto.


#inicio do controle de login
from estudo.models import User
# importa as rotas
from estudo.routes import homepage

login_manager=LoginManager(app)
bcrypt=Bcrypt(app)
# controle de login
login_manager.login_view='login'

# significa que você está usando o Flask-Login, mas não definiu a função obrigatória user_loader — que é necessária para o login funcionar corretamente.
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


