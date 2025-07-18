#pip install flask
from estudo import app
from flask import render_template, url_for 
from flask import redirect,flash
from flask_login import login_user, logout_user, current_user

from estudo.forms import UserForm, StoreForm


@app.route("/", methods=["GET","POST"])
def homepage():
      return render_template('index.html')


@app.route('/cadastrousuario/',methods=["GET","POST"])
def cadastrousuario():
    form=UserForm()
    if form.validate_on_submit():
        user=form.save()
        login_user(user, remember=True)
        flash('Cadastro realizado com sucesso! Você já está logado. ','success')
        return redirect(url_for('homepage'))


    return render_template('cadastrousuario.html', form=form)

@app.route('/cadastroloja/', methods=["GET","POST"])
def cadastroloja():
     form=StoreForm()
     if form.validate_on_submit():
         loja=form.save()
         login_user(loja, remember=True)
         flash('Cadastro realizado com sucesso! Você já está logado', 'success')
         return redirect(url_for('homepage'))
     
     
     return render_template('cadastroloja.html', form=form)
        

