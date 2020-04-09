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
	# Fazer requisicao de informacao via JSON
	dados = request.get_json()
	# Localização identificada por CEP
	localizacao = dados['localizacao']
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


	# Nivel da Temperatura

	NTP = 5

	if(temperatura >= 35.8 and temperatura <= 36.2):
		NTP = 1

	elif(temperatura >= 35.5 and temperatura < 35.8) or (temperatura > 36.2 and temperatura <= 36.5):
		NTP = 2

	elif(temperatura >= 35.2 and temperatura < 35.5) or (temperatura > 36.5 and temperatura <= 36.8):
		NTP = 3

	elif(temperatura >= 35 and temperatura < 35.2) or (temperatura > 36.8 and temperatura < 37):
		NTP = 4

	# Nivel de Pulsacao

	PU = 1

	if (pulso <= 60 or pulso > 100):
		PU = 5

	elif(pulso > 60 and pulso < 62) or (pulso > 90 and pulso <= 100):
		PU = 4

	elif(pulso >= 62 and pulso < 63) or (pulso > 80 and pulso <= 90):
		PU = 3

	elif(pulso >= 63 and pulso < 65) or (pulso > 70 and pulso <= 80):
		PU = 2

	# Nivel da Frequencia Respiratoria

	NFR = 1

	if(respiracao <= 12 or respiracao >= 20):
		NFR = 5

	elif(respiracao > 12 and respiracao <= 13) or (respiracao >= 19 and respiracao < 20):
		NFR = 4
	
	elif(respiracao > 13 and respiracao <= 14) or (respiracao >= 18 and respiracao < 19):
		NFR = 3

	elif(respiracao > 14 and respiracao <= 15) or (respiracao >= 16 and respiracao < 18):
		NFR = 2

	# Gravidade DA CS
	GCS = 5 if comorbidade else 1

	# Gerando 5 ou 1 com as Variaveis Patologicas 

	tosseSeca = 5 if tosseSeca else 1
	diarreia = 5 if diarreia else 1
	fApetite = 5 if fApetite else 1
	sabores = 5 if sabores else 1
	odores = 5 if odores else 1
	dorGarganta = 5 if dorGarganta else 1
	dorCorpo = 5 if dorCorpo else 1
	nariz = 5 if nariz else 1
	fadiga = 5 if fadiga else 1
	nausea = 5 if nausea else 1


	# Peso dos Sinais Vitais (Podem mudar de acordo com a porcentagem das ocorrencias em casos de COVID)
	
	t = 0.67
	pu = 0.03
	fr = 0.3

	# Peso dos Sinais Patologicos (Pode variar de acordo com a porcentagem de ocorrencia em casos de COVID)

	to = 0.51
	di = 0.02
	fa = 0.01
	sp = 0.08
	so = 0.01
	dg = 0.08
	dc = 0.09
	nc = 0.03
	fad = 0.22
	nau = 0.03

	# Calculo do valor de Tendencia Patologica com base nos pesos ditados

	TPA = (to * tosseSeca + di * diarreia + fa * fApetite + sp * sabores + so * odores + dg * dorGarganta + dc * dorCorpo + nc * nariz + fad * fadiga + nau * nausea)

	# Calculo do valor de Sinais Vitais 

	VSinais = (t * NTP + pu * PU + fr * NFR)

	# Calculo do Risco GUT

	RGUT = GCS * VSinais * TPA

	# Gerando resultados

	situacao = 1

	if(RGUT > 8 and RGUT <= 10):
		situacao = 2

	elif(RGUT > 10 and RGUT <= 44):
		situacao = 3

	elif(RGUT > 44 and RGUT < 53):
		situacao = 4

	elif(RGUT >= 53):
		situacao = 5

	return { 'situacao' : situacao }


def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    main()

