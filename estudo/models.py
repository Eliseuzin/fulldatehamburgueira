from estudo import db, login_manager
from datetime import datetime
from flask_login import UserMixin

# inicio do controle de login
@login_manager.user_loader
def load_user(user_id):
  return User.query.get(user_id)

class User(db.Model, UserMixin):
  id=db.Column(db.Integer, primary_key=True)
  nome=db.Column(db.String, nullable=True)
  sobrenome=db.Column(db.String, nullable=True)
  email=db.Column(db.String, nullable=True)
  senha=db.Column(db.String, nullable=True) 
#fim do  controle de login



class Contato(db.Model):
  id=db.Column(db.Integer, primary_key=True)
  # nullable=True, quer dizer que o valor nao pode ficar vazio
  nome=db.Column(db.String, nullable=True) 
  data_envio=db.Column(db.DateTime, default=datetime.utcnow())
  email=db.Column(db.String, nullable=True)
  assunto=db.Column(db.String, nullable=True)
  mensagem=db.Column(db.String, nullable=True)
  respostas=db.Column(db.Integer, default=0)

#para fazer roda as alteraçoes qualquer mudança
# flask db migrate -m "criação da tabela"
# flask db upgrade

# flask db migrate -m "corrigido campo nome"
# flask db upgrade
