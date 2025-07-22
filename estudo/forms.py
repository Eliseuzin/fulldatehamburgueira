#agora, iremos criar uma aplicaçao mais segura sobre o formulario e banco de dados
#1- instalar pip install flask_wtf
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,IntegerField
# EqualTo verifica se um campo é == ao outro
# para a validaçao do email precisamos instalar pip install email_validator
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

class UserForm(FlaskForm):
    nome= StringField('Nome', validators=[DataRequired()])
    sobrenome=StringField('Sobrenome', validators=[DataRequired()])
    email=StringField('Email', validators=[DataRequired()])
    senha=PasswordField('Senha', validators=[DataRequired()])
    confirmarsenha=PasswordField('Confirmar senha', validators=[DataRequired(), EqualTo('senha')])
    btnSubmit=SubmitField('Cadastrar usuário')
\
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