from flask import Flask, render_template, request, redirect;

app = Flask(__name__)

@app.route("/")
def login():
 return render_template("login.html")

@app.route("/painel")
def painel():
 return render_template("painel.html")

@app.route("/verificar", methods=['POST'])
def verificar():
    CPF = request.form.get('CPF')
    SENHA = request.form.get('SENHA')

    print('Tentando login com:', CPF, '/SENHA:',SENHA)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)