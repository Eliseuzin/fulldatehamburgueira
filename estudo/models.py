from estudo import login_manager
from flask_login import UserMixin

#inicio do controle de login
# significa que você está usando o Flask-Login, mas não definiu a função obrigatória user_loader — que é necessária para o login funcionar corretamente.
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):
    id=db.column(db.Integer,primary_key=True)
    nome=db.Column(db.String, nullable=True)
    sobrenome=db.Column(db.String, nullable=True)
    email=db.Column(db.String, nullable=True)
    senha=db.Column(db.String, nullable=True)
 #fim do controle de login