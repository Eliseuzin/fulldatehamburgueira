#pip install flask
from estudo import app
from flask import render_template, url_for 
from flask import redirect,flash
from flask_login import login_user, logout_user, current_user, login_required
from estudo.forms import LoginForm

from estudo.forms import UserForm, StoreForm


@app.route("/", methods=["GET", "POST"])
def homepage():
    # if current_user.is_authenticated:
    #     return f'Olá, {current_user.nome}!'
    # else:
        return render_template('index.html')



@app.route('/login/', methods=["GET", "POST"])
def login():
     form=LoginForm()

     if form.validate_on_submit():
        #aqui, não precisa validadar nada
        login_user(form.user, remember=True)
        flash('Login realizado com sucesso!','success')
        return redirect(url_for('homepage'))
     
     return render_template('login.html', form=form)   



@app.route('/cadastrousuario/',methods=["GET","POST"])
def cadastrousuario():
    form=UserForm()
    if form.validate_on_submit():
        user=form.save()
        login_user(user, remember=True)
        flash('Cadastro realizado com sucesso! Você já está logado. ','success')
        return redirect(url_for('homepage'))


    return render_template('cadastrousuario.html', form=form)

@app.route('/sair/')
def logout():
     logout_user()
     flash('Aguardamos você de volta!', 'danger')
     return redirect(url_for('homepage'))




@app.route('/cadastroloja/', methods=["GET","POST"])
def cadastroloja():
     form=StoreForm()
     if form.validate_on_submit():
         loja=form.save()
         login_user(loja, remember=True)
         flash('Cadastro realizado com sucesso! Você já está logado', 'success')
         return redirect(url_for('homepage'))
     
     
     return render_template('cadastroloja.html', form=form)
        
# rota de erro
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
