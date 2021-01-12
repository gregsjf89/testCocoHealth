################################################
##                                            ##
## API de prooftest para Teste da CocoHealth  ##
##                                            ##
################################################


# request para receber os nonvos clientes
from flask import Flask, jsonify, request

app = Flask(__name__)

clientes = [  # estrutura de dados
    {
        'id': '1',
        'nome': 'Gregory',
        'dob': '15/12/1989',
        'cpf': '37846058851',
        'tel': '123456789'
    }
]


@app.route('/')  # pagina inicial
def home():
    return "home"


@app.route('/clientes', methods=['GET'])  # retorna todos clientes
def pclientes():
    return jsonify(clientes), 200


# retorna cliente por cpf
@app.route('/clientes/<string:cpf>', methods=['GET'])
def clientes_per_cpf(cpf):
    clientes_per_cpf = [
        clientes for clientes in clientes if clientes['cpf'] == cpf]
    return jsonify(clientes_per_cpf), 200


# retorna cliente por nome
@app.route('/clientes/./<string:nome>', methods=['GET'])
def clientes_per_nome(nome):
    clientes_per_nome = [
        clientes for clientes in clientes if clientes['nome'] == nome]
    return jsonify(clientes_per_nome), 200


# inclui novo cliente dentro de "/clientes"
@app.route('/clientes', methods=['POST'])
def include_cliente():
    data = request.get_json()

    clientes.append(data)  # formato segue estrutura "clientes" acima

    return jsonify(data), 201  # retorna ok


@app.route('/clientes/<int:id>', methods=['DELETE'])
def remove_cliente(id):
    index = id - 1
    del clientes[index]

    return jsonify({'command': 'Cliente removido'}), 200


if __name__ == '__main__':
    app.run(debug=True)
