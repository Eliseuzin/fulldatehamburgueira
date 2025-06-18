from estudo import app
from flask import render_template, url_for  
#pip install flask
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
