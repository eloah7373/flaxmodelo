from flask import Flask, render_template, request, redirect, session;

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave-super-secreta'

@app.route("/")
def login():
 return render_template("login.html")

@app.route("/painel")
def painel():
  if 'usuario_nome' in session:
     return render_template("painel.html" , usuario_nome=session['usuario_nome'],usuario_cpf=session['usuario_cpf'])
  return redirect('/')

@app.route("/verificar", methods=['POST'])
def verificar():
    CPF = request.form.get('CPF')
    SENHA = request.form.get('SENHA')

    print('Tentando login com:', CPF, '/SENHA:',SENHA)
    if CPF == "12345678910" and SENHA == "123":
       session['usuario_nome'] = "Eloah"
       session['usuario_cpf'] = CPF
       return redirect('/painel')
    if CPF == "12345678911" and SENHA == "321":
           session['usuario_nome'] = "Diego"
           session['usuario_cpf'] = CPF
           return redirect('/painel')

    
    
    return redirect('/')
@app.route('/sair')
def sair():
   session.pop ('usuario_nome',None)
   session.pop('usuario_cpf', None)
   return  redirect('/')



if __name__ == "__main__":
    app.run(debug=True)