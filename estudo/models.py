from estudo import db
from datetime import datetime
from flask_login import UserMixin

#inicio do controle de login usuario
# significa que você está usando o Flask-Login, mas não definiu a função obrigatória user_loader — que é necessária para o login funcionar corretamente.

class User(db.Model,UserMixin):
    #nullable=True, que dizer que o campo não pode ficar vazio
    id=db.Column(db.Integer,primary_key=True)
    nome=db.Column(db.String, nullable=True)
    endereco=db.Column(db.String, nullable=True)
    complemento=db.Column(db.String, nullable=True)
    celular=db.Column(db.Integer, nullable=True)
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
    celularp=db.Column(db.Integer, nullable=True)
    senha=db.Column(db.String, nullable=True)
    cnpj=db.Column(db.Integer, nullable=True)
    nomedaloja=db.Column(db.String, nullable=True)
    telefone=db.Column(db.Integer, nullable=True)
    endereço=db.Column(db.String, nullable=True)
 #fim do controle de login loja

#inicio de salvar itens do carrinho
class Carrinho(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    itens = db.relationship('ItemCarrinho', backref='carrinho', lazy=True)

class ItemCarrinho(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    carrinho_id = db.Column(db.Integer, db.ForeignKey('carrinho.id'))
    nome_produto = db.Column(db.String(100))
    preco = db.Column(db.Float)
    quantidade = db.Column(db.Integer)

#fim de salvar itens do carrinho




#comando para criar o banco de dados
#flask db init
#é necessário apenas um banco de dados por projeto.
# para fazer roda as alteraçoes no banco de dados
# flask db migrate -m "mensagem"
# flask db upgrade