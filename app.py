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
	pulso = dados['pulso']
	respiracao = dados['respiracao']
	tosseSeca = dados['tosseSeca']
	diarreia = dados['diarreia']
	fApetite = dados['fApetite']
	odores = dados['odores']
	sabores = dados['sabores']
	dorGarganta = dados['dorGarganta']
	dorCorpo = dados['dorCorpo']
	nariz = dados['nariz']
	fadiga = dados['fadiga']
	nausea = dados['nausea']
	#Definindo variaveis previamente
	idoso = 0
	sangue = 0
	pulmao = 0
	febre = 0

	if idade > 50:
		idoso = 1

	if temperatura > 37:
		febre = 1
	
	if pulso < 60:
		sangue = 1

	if respiracao > 20:
		pulmao = 1
	
	if (comorbidade == 0):
		if (febre == 0) and ((tosseSeca == 0) or (nariz == 0) or (dorGarganta == 0) or (pulmao == 0)):
			return { 'situacao' : 'Situaçao 1'}
		else:
			if idoso == 1 :
				return { 'situacao' : 'Situaçao 4'}
			else:
				return { 'situacao' : 'Situaçao 2'}

	else:
		if (febre == 0) and ((tosseSeca == 0) or (nariz == 0) or (dorGarganta == 0) or (pulmao == 0)):
			if idoso == 1:
				return {'situacao' : 'Situação 5'}

			else:
				return {'situacao' : 'Situação 3'}


def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    main()
