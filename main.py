
from flask import Flask, jsonify, make_response, request
from bd import Campos



app = Flask('campos')

@app.route('/campos', methods=['GET'])
def get_campos():
    return Campos

@app.route('/campos/<int:id>', methods=['GET'])
def get_campo(id):
    for campo in Campos:
        if  campo.get('id') == id:
            return jsonify(campo)

@app.route('/campos', methods=['POST'])
def criar_campo():
    campo = request.json
    Campos.append(campo)
    return make_response(
        jsonify(mensagem='Campo cadastrado!',
                campo=campo)
    )

@app.route('/campos/<int:id>', methods=['PUT'])
def editar_campos(id):
    campo_alterado = request.get_json()
    for indice, campo in enumerate(Campos):
        if campo.get('id') == id:
            Campos[indice].update(campo_alterado)
            return jsonify(Campos[indice])
        

@app.route('/campos/<int:id>', methods=['DELETE'])
def deletar_campo(id):
    for indice, campo in enumerate(Campos):
        if campo.get('id') == id:
            del Campos[indice]
            return jsonify({"mensagem": "Campo deletado com sucesso!"})


app.run(port=5000, host='localhost')