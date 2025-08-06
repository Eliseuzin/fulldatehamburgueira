#pip install flask
from estudo import app,db
from flask import render_template, url_for 
from flask import redirect,flash
from flask_login import login_user, logout_user, current_user, login_required
from estudo.forms import LoginForm
from flask import session, request, jsonify
from estudo.models import ItemCarrinho, Carrinho

#AGORA, IREMOS CRIAR OS PASSOS DE Pedir link de recuperação
 # função que você deve implementar
# from flask import render_template, request, flash, redirect, url_for
from estudo.forms import PedidoRecuperacaoForm
from estudo.utils import gerar_token,enviar_email
from estudo.models import User  # seu modelo de usuário

# E Página para redefinir senha
from estudo.forms import RedefinirSenhaForm
from estudo.utils import verificar_token
from werkzeug.security import generate_password_hash

from estudo.forms import AtualizarUsuarioForm  # ou ajuste o nome conforme necessário



from estudo.forms import UserForm, StoreForm


@app.route("/", methods=["GET", "POST"])
def homepage():
    # if current_user.is_authenticated:
    #     return f'Olá, {current_user.nome}!'
    # else:
        return render_template('index.html')



@app.route('/login/', methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        login_user(form.user, remember=True)

        # Aqui começa o salvamento do carrinho da sessão
        carrinho_session = session.get('carrinho')
        if carrinho_session:
            # Apaga carrinho antigo do usuário
            carrinho_antigo = Carrinho.query.filter_by(user_id=form.user.id).first()
            if carrinho_antigo:
                db.session.delete(carrinho_antigo)
                db.session.commit()

            # Cria novo carrinho vazio
            carrinho_db = Carrinho(user_id=form.user.id)
            db.session.add(carrinho_db)
            db.session.commit()


            for item_sessao in carrinho_session:
                item_existente = ItemCarrinho.query.filter_by(
                    carrinho_id=carrinho_db.id,
                    nome_produto=item_sessao['nome_produto']
                ).first()

                if item_existente:
                    item_existente.quantidade += item_sessao['quantidade']
                else:
                    novo_item = ItemCarrinho(
                        carrinho_id=carrinho_db.id,
                        nome_produto=item_sessao['nome_produto'],
                        preco=item_sessao['preco'],
                        quantidade=item_sessao['quantidade']
                    )
                    db.session.add(novo_item)

            db.session.commit()
            session.pop('carrinho', None)  # limpa a sessão

        # Aqui termina

        flash('Login realizado com sucesso!', 'success')
        return redirect(url_for('homepage'))

    return render_template('login.html', form=form)


@app.route('/meu-carrinho', methods=['GET'])
@login_required
def meu_carrinho():
    carrinho = Carrinho.query.filter_by(user_id=current_user.id).first()
    if not carrinho:
        return jsonify([])

    itens = []
    for item in carrinho.itens:
        itens.append({
            'name': item.nome_produto,
            'price': item.preco,
            'quantity': item.quantidade
        })

    return jsonify(itens)

  



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


#rota para salvar carrinho
@app.route('/adicionar-carrinho', methods=['POST'])
def adicionar_carrinho():
    dados = request.get_json()

    novo_item = {
        'nome_produto': dados.get('nome_produto'),
        'preco': float(dados.get('preco')),
        'quantidade': int(dados.get('quantidade', 1))
    }

    if 'carrinho' not in session:
        session['carrinho'] = []

    # Verifica se já existe o produto no carrinho
    carrinho = session['carrinho']
    for item in carrinho:
        if item['nome_produto'] == novo_item['nome_produto']:
            item['quantidade'] += novo_item['quantidade']
            break
    else:
        carrinho.append(novo_item)

    session['carrinho'] = carrinho
    session.modified = True

    return jsonify({'mensagem': 'Item adicionado ao carrinho'})

#AGORA, IREMOS CRIAR OS PASSOS DE Pedir link de recuperação
 # função que você deve implementar

@app.route('/recuperar-senha', methods=['GET', 'POST'])
def recuperar_senha():
    form = PedidoRecuperacaoForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            token = gerar_token(user.email)
            link = url_for('redefinir_senha', token=token, _external=True)

            # Renderiza o template do e-mail com o link
            corpo_email = render_template('email_redefinir_senha.html', link=link)

            enviar_email(user.email, 'Redefinir sua senha', corpo_email)
            flash('Enviamos um link para redefinir sua senha no seu email.', 'info')
            return redirect(url_for('login'))

        else:
            flash('Email não encontrado.', 'warning')
        # return redirect(url_for('login'))
    return render_template('recuperar_senha.html', form=form)



# E Página para redefinir senha
@app.route('/redefinir-senha/<token>', methods=['GET', 'POST'])
def redefinir_senha(token):
    email = verificar_token(token)
    if not email:
        flash('O link é inválido ou expirou.', 'danger')
        return redirect(url_for('recuperar_senha'))

    form = RedefinirSenhaForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=email).first()
        if user:
            user.senha = generate_password_hash(form.senha.data)
            db.session.commit()
            flash('Sua senha foi redefinida com sucesso.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Usuário não encontrado.', 'danger')
            return redirect(url_for('recuperar_senha'))

    return render_template('redefinir_senha.html', form=form)


#atualizar cadastro

@app.route('/atualizar_cadastro', methods=['GET', 'POST'])
@login_required
def atualizar_cadastro():
    form = AtualizarUsuarioForm(obj=current_user)  # Pré-preenche os dados do usuário

    if form.validate_on_submit():
        # Atualizar os dados
        current_user.nome = form.nome.data
        current_user.sobrenome = form.sobrenome.data
        current_user.email = form.email.data

        # Atualiza a senha somente se o campo não estiver vazio
        if form.senha.data:
            current_user.senha = generate_password_hash(form.senha.data)

        db.session.commit()
        flash('Seus dados foram atualizados com sucesso!', 'success')
        return redirect(url_for('homepage'))

    return render_template('atualizar_cadastro.html', form=form)
