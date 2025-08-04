#agora, iremos criar uma aplicaçao mais segura sobre o formulario e banco de dados
#1- instalar pip install flask_wtf
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,IntegerField, TextAreaField
# EqualTo verifica se um campo é == ao outro
# para a validaçao do email precisamos instalar pip install email_validator
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from estudo import db, bcrypt
from estudo.models import User,Store

#recuperaçao de senha
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
# from wtforms.validators import DataRequired, Email

#redefinir senha
# from flask_wtf import FlaskForm
# from wtforms import PasswordField, SubmitField
# from wtforms.validators import DataRequired, EqualTo

class UserForm(FlaskForm):
    nome= StringField('Nome', validators=[DataRequired()])
    sobrenome=StringField('Sobrenome', validators=[DataRequired()])
    email=StringField('Email', validators=[DataRequired()])
    senha=PasswordField('Senha', validators=[DataRequired()])
    confirmarsenha=PasswordField('Confirmar senha', validators=[DataRequired(), EqualTo('senha')])
    btnSubmit=SubmitField('Cadastrar usuário')

    def save(self):
        senha=bcrypt.generate_password_hash(self.senha.data.encode('utf-8'))
        user=User(
            nome=self.nome.data,
            sobrenome=self.sobrenome.data,
            email=self.email.data,
            senha=senha
        )
        db.session.add(user)
        db.session.commit()
        return user
#  class Loginform(FlaskForm):


class StoreForm(FlaskForm):
    nome=StringField('Nome', validators=[DataRequired()])
    sobrenome=StringField('Sobrenome', validators=[DataRequired()])
    email=StringField('Email', validators=[DataRequired()])
    senha=PasswordField('Senha', validators=[DataRequired()])
    confirmarsenha=PasswordField('Confirmar senha', validators=[DataRequired()])
    cnpj=IntegerField('CNPJ da loja', validators=[DataRequired()])
    nomedaloja=StringField('Nome da loja', validators=[DataRequired()])
    telefone=IntegerField('Telefone da loja', validators=[DataRequired()])
    endereço=StringField('Endereço da loja', validators=[DataRequired()])
    btnSubmit=SubmitField('Cadastrar loja')

class LoginForm(FlaskForm):
    email=StringField('E-mail', validators=[DataRequired(),Email()])
    senha=PasswordField('Senha', validators=[DataRequired()])
    btnSubmit=SubmitField('Entrar')

    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if not user:
            raise ValidationError('E-mail não encontrado, por favor, verifique o e-mail digitado!')
        # armazenar o usuario encontrado
        self.user=user
    
    def validate_senha(self,senha):
        # só valida se o email for valido e usuário existir
        user=getattr(self,'user',None)
        if user is None:
             #  evita validação dupla caso o email falhar
             return
        if not bcrypt.check_password_hash(user.senha,senha.data.encode('utf-8')):
            raise ValidationError('Senha incorreta, por favor, verifique a senha digitada!')
        


class PedidoRecuperacaoForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Enviar link de recuperação')



class RedefinirSenhaForm(FlaskForm):
    senha = PasswordField('Nova senha', validators=[DataRequired()])
    confirmar_senha = PasswordField('Confirmar senha', validators=[
        DataRequired(),
        EqualTo('senha', message='As senhas devem ser iguais.')
    ])
    submit = SubmitField('Redefinir senha')
