from flask import Flask, jsonify, request, json
app = Flask(__name__)

desenvolvedores = [
    {'nome':'Carlos', "habilidades":['Python', 'Flask']},

    {'nome':'João',
     'habilidades':['Python', 'Django']}
]

#Devolve um desenvelvedor pelo ID, tabém altera e deleta um desenvolvedor
@app.route("/dev/<int:id>", methods = ['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        desenvolvedor = desenvolvedores[id]
        print(desenvolvedor)
        return jsonify(desenvolvedor)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({"Status": "deletado com sucesso"})

#Lista todos os desenvolvedores e permite registar um novo desenvolvedor
@app.route("/dev/", methods = ['POST', 'GET'])
def list_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        desenvolvedores.append(dados)

        return jsonify('Status":"sucesso", "mensagem":"registro inserido"')


if __name__ == '__main__':
    app.run(debug=True)
