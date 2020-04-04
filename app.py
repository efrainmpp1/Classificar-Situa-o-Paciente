import os
from flask import Flask ,  request
from flask_cors import CORS
import json

app = Flask(__name__)

cors = CORS(app, resource={r"/*":{"origins": "*"}})

@app.route("/", methods=['GET'])
def index():
    return "<h1>Teste APP Classificador de Situações!</h1>"

@app.route('/classificar' , methods=['POST' , 'GET'])
def classificar():
	dados = request.get_json()
	idade = dados['idade']
	comorbidade = dados['comorbidade']
	contatoSuspeito = dados['contatoSuspeito']
	temperatura = dados['temperatura']
	respiracao = dados['respiracao']
	tosseSeca = dados['tosseSeca']
	dorGarganta = dados['dorGarganta']
	#Definindo variaveis previamente
	idoso = False
	pulmao = False
	febre = False

	if idade > 50:
		idoso = True

	if temperatura > 37:
		febre = True

	if respiracao > 20:
		pulmao = True

	# sintomas gripais, caso tenha febre e pelo menos um dos casos abaixo
	sintomas_gripais = febre and (tosseSeca or nariz or dorGarganta or pulmao)
	
	situacao = 1

	if comorbidade and sintomas_gripais :
		situacao = 5 if idoso else 3

	elif sintomas_gripais:
		situacao = 4 if idoso else 2

	elif comorbidade and febre :
		situacao = 2

	return {'situacao' : situacao}

def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    main()
