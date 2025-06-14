from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
# EqualTo verifica se um campo é == ao outro
# para a validaçao do email precisamos instalar pip install email_validator
from estudo import db, bcrypt
from estudo.models import Contato, User


class Userform(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    sobrenome = StringField('Sobrenome', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    confirmarsenha = PasswordField('Confirmar_senha', validators=[
                                   DataRequired(), EqualTo('senha')])
    btnSubmit = SubmitField('Cadastrar')

    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError('Usuário já cadastrado com este E-mail !!!')
        
    def save(self):
        senha = bcrypt.generate_password_hash(
            self.senha.data.encode('utf-8'))
        user = User(
            nome=self.nome.data,
            sobrenome=self.sobrenome.data,
            email=self.email.data,
            senha=senha
        )
        db.session.add(user)
        db.session.commit()
        return user
    

class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    btnSubmit = SubmitField('Login')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if not user:
            raise ValidationError('E-mail não encontrado, por favor tente novamente!')
        # Armazenar o usuário encontrado
        self.user = user

    def validate_senha(self, senha):
        # Só valida se o email for válido e usuário encontrado
        user = getattr(self, 'user', None)
        if user is None:
            return  # evita validação dupla caso o email já falhou
        if not bcrypt.check_password_hash(user.senha, senha.data.encode('utf-8')):
            raise ValidationError('Senha incorreta, verifique novamente!')

class Contatoform(FlaskForm):
    # () nomes do label
    nome = StringField('nome', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    assunto = StringField('assunto', validators=[DataRequired()])
    mensagem = TextAreaField('mensagem', validators=[DataRequired()])
    btnSubmit = SubmitField('Enviar', validators=[DataRequired()])

    def save(self):
        contato = Contato(
            nome=self.nome.data,
            email=self.email.data,
            assunto=self.assunto.data,
            mensagem=self.mensagem.data
        )
        db.session.add(contato)
        db.session.commit()
