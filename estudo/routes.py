from estudo import app, db, bcrypt
from flask import render_template, request
from flask import redirect, url_for,flash
from flask_login import login_user, logout_user, current_user

from estudo.models import Contato, User
from estudo.forms import Contatoform, Userform, LoginForm
# currentuser verifica se o usuário esta logado

# @app.route("/")
# def homepage():
#     return redirect(url_for("sport"))

@app.route("/", methods=["GET", "POST"])
def homepage():
    usuario = "eliseu"
    idade = 24
    estado_civil = "solteiro"
    form = LoginForm()

    if form.validate_on_submit():
        # Aqui não precisa mais validar nada!
        login_user(form.user, remember=True)
        flash('Login realizado com sucesso!', 'success')
        return redirect(url_for('homepage'))

    dici = {
        'usuario': usuario,
        'idade': idade,
        'estado_civil': estado_civil
    }
    return render_template("index.html", dici=dici, form=form)

@app.route('/cadastro/', methods=["GET", "POST"])
def cadastro():
    form=Userform()
    if form.validate_on_submit():
        user=form.save()
        login_user(user, remember=True)
        flash('Cadastro realizado com sucesso! Você já está logado.', 'success')
        return redirect(url_for('homepage'))
    # print('cadastro')
    return render_template('cadastro.html', form=form)


@app.route('/sair/')
def logout():
    logout_user()
    flash('Aguardamos novamente!!!.', 'danger')
    return redirect(url_for('homepage'))


@app.route("/contato/", methods=["GET", "POST"])
def   contato():
    form=Contatoform()
    context={}
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('homepage'))
    return render_template('contato.html', context=context,form=form)

@app.route('/contato/lista')
def contatolista():
    if request.method == 'GET':
       pesquisa = request.args.get('pesquisa', '')

    dados = Contato.query.order_by(Contato.nome)
    if pesquisa != '':
          dados = dados.filter_by(nome = pesquisa)
    # print(dados)
    context = {'dados':dados.all()}

    # for linha in dados:
    #     print(linha.nome)
    #     print(linha.email)
    return render_template('lista_contatos.html', context=context)

# rota dinamica
# id, pode ser qualquer nome
#colocando uma / no final evitar que o navegador entre com barras eleatorias na url
@app.route('/contato/<int:id>/')
def contatoinfodados(id):
    obj=Contato.query.get(id)
# passa o id para ver se esta funcionando, no return
    return render_template('contato_detail.html',obj=obj)

#forma nao recomendada
# def contato():
#     form=Contatoform()
#     nome = None
#     if request.method == "POST":
#         none = request.form.get("nome")
#         email=request.form.get('email')
#         assunto=request.form.get('assunto')
#         mensagem=request.form.get('mensagem')

#         contato=Contato(
#             none=none,
#             email=email,
#             assunto=assunto,
#             mensagem=mensagem
#         )
#         db.session.add(contato)
#         db.session.commit()

#     elif request.method == "GET":
#         nome = request.args.get("nome")

#     return render_template("contato.html", nome=nome, form=form)

#formato não recomendado para formulários
# @app.route("/contato_old/", methods=["GET", "POST"])
# def contato_old():
#     nome = None
#     if request.method == "POST":
#         none = request.form.get("nome")
#         email=request.form.get('email')
#         assunto=request.form.get('assunto')
#         mensagem=request.form.get('mensagem')

#         contato=Contato(
#             none=none,
#             email=email,
#             assunto=assunto,
#             mensagem=mensagem
#         )
#         db.session.add(contato)
#         db.session.commit()

#     elif request.method == "GET":
#         nome = request.args.get("nome")

#     return render_template("contato_old.html", nome=nome)


