from estudo import db
from datetime import datetime
from flask_login import UserMixin

#inicio do controle de login usuario
# significa que você está usando o Flask-Login, mas não definiu a função obrigatória user_loader — que é necessária para o login funcionar corretamente.

class User(db.Model,UserMixin):
    #nullable=True, que dizer que o campo não pode ficar vazio
    id=db.Column(db.Integer,primary_key=True)
    nome=db.Column(db.String, nullable=True)
    sobrenome=db.Column(db.String, nullable=True)
    email=db.Column(db.String, nullable=True)
    senha=db.Column(db.String, nullable=True)
 #fim do controle de login usuario

 #inicio do controle de login loja
class Store(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    nome=db.Column(db.String, nullable=True)
    sobrenome=db.Column(db.String, nullable=True)
    email=db.Column(db.String, nullable=True)
    senha=db.Column(db.String, nullable=True)
    cnpj=db.Column(db.Integer, nullable=True)
    nomedaloja=db.Column(db.String, nullable=True)
    telefone=db.Column(db.Integer, nullable=True)
    endereço=db.Column(db.String, nullable=True)
 #fim do controle de login loja

#comando para criar o banco de dados
#flask db init
#é necessário apenas um banco de dados por projeto.
# para fazer roda as alteraçoes no banco de dados
# flask db migrate -m "mensagem"
# flask db upgrade