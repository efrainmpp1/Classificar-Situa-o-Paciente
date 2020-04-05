import os
from flask import Flask ,  request
from flask_cors import CORS
import json

app = Flask(__name__)

cors = CORS(app, resource={r"/*":{"origins": "*"}})

lista_pessoas = []
lista_IDs = []

@app.route("/", methods=['GET'])
def index():
    return "<h1>Teste APP Classificador de Situações!</h1>"


@app.route('/classificar' , methods=['POST' , 'GET'])
def classificar():
	# Chamo as listas globais que serão modificadas dentro da funcao 
	global lista_pessoas
	global lista_IDs
	# Fazer requisicao de informacao via JSON
	dados = request.get_json()
	idade = dados['idade']
	comorbidade = dados['comorbidade']
	user_ID = dados['user_ID']

	#Caso nao exista o ID do usuario na lista de usuarios,adicionamos esse usuario 
	if not (user_ID in lista_IDs):
		lista_IDs.append(user_ID)
		lista_pessoas[user_ID] = criarDicionario()

	# Crio um laço for para cadastrar no dicionario da pessoa as novas informacoes nas listas internas (Não sei se funciona)
	for k in lista_pessoas[user_ID]:
		lista_pessoas[user_ID][k].append(dados[k])

	# Criar variaveis que buscam o caso mais pessimista e alocar elas na lista que sera usada para fazer a analise da situacao

	temperatura = lista_pessoas[user_ID]['temperatura'].max()
	respiracao = lista_pessoas[user_ID]['frquenciaRespiratória'].max()
	contatoSuspeito = gerarbool(lista_pessoas[user_ID]['contatoSuspeito'])
	tosseSeca = gerarbool(lista_pessoas[user_ID]['tosseSeca'])
	dorGarganta = gerarbool(lista_pessoas[user_ID]['doresnaGarganta'])
	nariz = gerarbool(lista_pessoas[user_ID]['narizCongestionado'])

	#Definindo variaveis previamente
	idoso = idade > 60
	febre = temperatura > 37
	sangue = pulso < 60
	pulmao = respiracao > 20

	# sintomas gripais, caso tenha febre e um pelo menos um dos casos a baixo
	sintomas_gripais = febre and (tosseSeca or nariz or dorGarganta or pulmao)
	
	situacao = 1
	if not comorbidade and sintomas_gripais:
		situacao = 4 if idoso else 2

	elif sintomas_gripais:
		situacao = 5 if idoso else 3

	return {'situacao': situacao}
	

def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    main()

# Funcao que cria um novo dicionario para o usuario  
def criarDicionario():
	return {
	'temperatura' : [],
	'contatoSuspeito' : [] ,
	'frquenciaRespiratória' : [] ,  
	'tosseSeca' : [] , 
	'doresnaGarganta' : [] ,
	'narizCongestionado ' : [] ,
	}

# Funcao  gerar um booleano analizando uma certa lista
def gerarbool(lista):
	return True if (True in lista) else False