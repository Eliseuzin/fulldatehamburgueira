from estudo import db
from datetime import datetime
from flask_login import UserMixin

#inicio do controle de login
# significa que você está usando o Flask-Login, mas não definiu a função obrigatória user_loader — que é necessária para o login funcionar corretamente.

class User(db.Model,UserMixin):
    #nullable=True, que dizer que o campo não pode ficar vazio
    id=db.Column(db.Integer,primary_key=True)
    nome=db.Column(db.String, nullable=True)
    sobrenome=db.Column(db.String, nullable=True)
    email=db.Column(db.String, nullable=True)
    senha=db.Column(db.String, nullable=True)
 #fim do controle de login