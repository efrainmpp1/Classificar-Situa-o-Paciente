import os
from flask import Flask , jsonify
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app, resource={r"/*":{"origins": "*"}})

@app.route("/", methods=['GET'])
def index():
    return "<h1>Hello World!</h1>"

@app.route("/secundaria", methods=['GET'])    
def secundaria():
    return "<h1>Pagina Secundaria </h1>"

@app.route("/testejson/<temperatura>") 
def testejson(temperatura):
	return jsonify({"ObjetoTemperatura" : "{}"}).format(temperatura)

def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    main()
