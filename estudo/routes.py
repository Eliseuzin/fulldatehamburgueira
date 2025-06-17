from estudo import app  
#pip install flask
@app.route('/', methods=["GET","POST"])
def homepage():
    usuario='eliseu'
    idade=24
    estado_civil='solteiro'