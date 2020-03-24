import os
from flask import Flask , jsonify , request
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app, resource={r"/*":{"origins": "*"}})

@app.route("/", methods=['GET'])
def index():
    return "<h1>Hello Efrain!</h1>"

@app.route("/secundaria", methods=['GET'])    

def secundaria():
    return "<h1>Pagina Secundaria </h1>"

@app.route("/testejson") 
def testejson():
	return jsonify({"ObjetoTemperatura" : 'temperatura'})


@app.route('/processojson' , methods=['POST'])
def processocomjson():
	dados = request.get_json()

	nome = dados['nome']

	localizacao = dados['localizacao']

	temperatura = dados['temperatura']

	return jsonify({'enviado' : 'ok' , 'nome' : nome , 'localizacao' : localizacao , 'temperatura' : temperatura})

def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    main()
