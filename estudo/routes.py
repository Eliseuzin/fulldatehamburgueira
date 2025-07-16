#pip install flask
from estudo import app
from flask import render_template, url_for 
from flask import redirect,flash

# inicio da nosso controle de login.
# pip install flask-login flask-bcrypt 
@app.route("/", methods=["GET","POST"])
def homepage():
      return render_template('index.html')
    # usuario="eliseu"
    # idade=24
    # estado_civil="solteiro"

    # dici={
    #     'usuario': usuario,
    #     'idade':idade,
    #     'estado_civil':estado_civil
    #  }
@app.route('/cadastro/',methods=["GET","POST"])
def cadastro():
      return render_template('cadastro.html')
  # form=Userform()
  # if form.validate_on_submit():
  #   user=form.save()
  #   flash(f'Usuario{user.username}Cadastrodo com sucesso! ',' success')
  #   return redirect(url_for('homepage'))
  # return render_template('cadastro.html', form=form)
