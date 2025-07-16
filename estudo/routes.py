#pip install flask
from estudo import app
from flask import render_template, url_for 
from flask import redirect,flash
from flask_login import login_user, logout_user, current_user

from estudo.forms import UserForm


@app.route("/", methods=["GET","POST"])
def homepage():
      return render_template('index.html')

@app.route('/cadastro/',methods=["GET","POST"])
def cadastro():
    form=UserForm()
    if form.validate_on_submit():
        user=form.save()
        login_user(user, remember=True)
        flash('Cadastro realizado com sucesso! Você já logado. ','success')


    return render_template('cadastro.html')
