from estudo import app
from flask import render_template  
#pip install flask
@app.route('/', methods=["GET","POST"])
def homepage():
    usuario='eliseu'
    idade=24
    estado_civil='solteiro'

    dici={
        'usuario': usuario,
        'idade':idade,
        'estado_civil':estado_civil
     }
    return render_template('index.html', dici=dici)