from estudo import app
#rodar o projeto, apenas quem estiver chamando main
if __name__=="__main__":
  #sempre que acontecer uma mudança ele estará iniciando novamente
  app.run(debug=True)