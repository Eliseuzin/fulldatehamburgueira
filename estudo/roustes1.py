#pip install flask
from estudo import app
from flask import render_template, url_for 
# inicio da nosso controle de login.
# pip install flask-login flask-bcrypt 
@app.route("/", methods=["GET","POST"])
def homepage():
      return render_template('index.html')


@app.route("/cadastro/", methods=["GET","POST"])
def cadastro():
      return render_template("cadastro.html")

