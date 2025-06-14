#modelo de python

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
# inicio da nosso controle de login.
# pip install flask-login flask-bcrypt
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
# responsavel por busca os valores
import os
load_dotenv('.env')


#instartar nossa aplicativo
app=Flask(__name__)
#configurar o banco de dados
#quando criarmos o banco de dados ele chamará database.db
app.config['SQLALCHEMY_DATABASE_URI']=os.getenv('DATABASE_URI')
#aumentar a prioridade, e evitar o check
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
#mais para frente aprenderemos trazer mais segurança ao banco de dados,e nunca deixa a chave expostar
app.config['SECRET_KEY']=os.getenv('SECRET_KEY')

db=SQLAlchemy(app)
migrate = Migrate(app, db)
#comando para de fato criar o database
#flask db init
#é necessario da apenas um comando por projeto

login_manager=LoginManager(app)
bcrypt=Bcrypt(app)
# controle de login
login_manager.login_view='login'

from estudo.routes import homepage
from estudo.models import Contato

#vamos começa a configura o nosso banco de dados
#pip install Flask-SQLAlchemy Flask-Migrate
#depois temos de import antes de app
# PowerShell

# vamos deixa nosso nossas chaves mais seguras utilizando variaveis de ambiente
# pip install python-dotenv
