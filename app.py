import os
from os.path import isfile
from flask import Flask , jsonify , request
from flask_cors import CORS
#from json import dump , load

def lerjson():
	with open('dados.json' , 'r' , encoding='utf8') as f:
		return load(f)

app = Flask(__name__)

cors = CORS(app, resource={r"/*":{"origins": "*"}})

@app.route("/", methods=['GET'])
def index():
    return "<h1>Teste APP PROCESSOS DE DADOS!</h1>"

'''
@app.route('/processojson' , methods=['POST'])
def processocomjson():
	dados = request.get_json()

	nome = dados['nome']

	localizacao = dados['localizacao']

	temperatura = dados['temperatura'] 

	dados = lerjson()

	localizacao = dados['localizacao']

	temperatura = dados['temperatura']

	diarreia = dados['diarreia']

	espirro = dados['espirro']

	return jsonify({'entregue' : 'ok' , 'localizacao' : localizacao , 'temperatura' : temperatura , 'diarreia' : diarreia , 'espirro' : espirro})

'''

def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    main()
