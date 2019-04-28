from flask import Flask, url_for, request, json, jsonify, abort
from json import dumps
from datetime import datetime
import decimal

from fornecedores import Fornecedores
from vendedores import Vendedores
from categorias import Categorias
from produtos import Produtos
from compras import Compras
from vendas import Vendas

app = Flask(__name__)


@app.route('/')
def root():
    return 'Seja bem-vindo!'

### Inicio metodos criacao de tabelas
@app.route('/createTableFornecedores')
def createFornecedor():
    fornecedores = Fornecedores()
    if (fornecedores.createTable()):
        result = {"result": "Tabela de fornecedores criada!"}
    else:
        result = {"result": "Problema para criar tabela de fornecedores!"}
    return jsonify(result)


@app.route('/createTableVendedores')
def createVendedores():
    vendedores = Vendedores()
    if (vendedores.createTable()):
        result = {"result": "Tabela de vendedores criada!"}
    else:
        result = {"result": "Problema para criar tabela de vendedores!"}
    return jsonify(result)


@app.route('/createTableCategorias')
def createCategorias():
    categorias = Categorias()
    if (categorias.createTable()):
        result = {"result": "Tabela de categorias criada!"}
    else:
        result = {"result": "Problema para criar tabela de categorias!"}
    return jsonify(result)


@app.route('/createTableProdutos')
def createProdutos():
    produtos = Produtos()
    if (produtos.createTable()):
        result = {"result": "Tabela de produtos criada!"}
    else:
        result = {"result": "Problema para criar tabela de produtos!"}
    return jsonify(result)


@app.route('/createTableCompras')
def createCompras():
    compras = Compras()
    if (compras.createTable()):
        result = {"result": "Tabela de Compras criada!"}
    else:
        result = {"result": "Problema para criar tabela de Compras!"}
    return jsonify(result)


@app.route('/createTableVendas')
def createVendas():
    vendas = Vendas()
    if (vendas.createTable()):
        result = {"result": "Tabela de Vendas criada!"}
    else:
        result = {"result": "Problema para criar tabela de Vendas!"}
    return jsonify(result)

### Fim metodos criacao de tabelas

### Inicio metodos de insert
@app.route('/insertVendedor', methods=['POST'])
def insertVendedor():

    if not request.json:
        abort(400)
    req_data = request.get_json()

    cpf = req_data['cpf']
    nome = req_data['nome']
    carteiraTrabalho = req_data['carteiraTrabalho']
    telefone = req_data['telefone']

    vendedores = Vendedores()

    if(vendedores.insertVendedor(cpf, nome, carteiraTrabalho, telefone)):
        result = {"result": "Dados inseridos com sucesso"}
    else:
        result = {"result": "Problemas para inserir os dados"}
    return jsonify(result)

@app.route('/insertFornecedor', methods=['POST'])
def insertFornecedor():
    if not request.json:
        abort(400)
    req_data = request.get_json()

    cnpj = req_data['cnpj']
    razaoSocial = req_data['razaoSocial']
    telefone = req_data['telefone']
    endereco = req_data['endereco']
    contato = req_data['contato']

    fornecedores = Fornecedores()

    if(fornecedores.insertFornecedor(cnpj, razaoSocial, telefone, endereco, contato)):
        result = {"result": "Dados inseridos com sucesso"}
    else:
        result = {"result": "Problemas para inserir os dados"}
    return jsonify(result)


@app.route('/insertCategoria', methods=['POST'])
def insertCategoria():
    if not request.json:
        abort(400)
    req_data = request.get_json()

    tituloCategoria = req_data['tituloCategoria']
    descricaoCategoria = req_data['descricaoCategoria']

    categorias = Categorias()

    if(categorias.insertCategoria(tituloCategoria, descricaoCategoria)):
        result = {"result": "Dados inseridos com sucesso"}
    else:
        result = {"result": "Problemas para inserir os dados"}
    return jsonify(result)


@app.route('/insertProduto', methods=['POST'])
def insertProduto():
    if not request.json:
        abort(400)
    req_data = request.get_json()

    id_fornecedor = req_data['id_fornecedor']
    id_categoria = req_data['id_categoria']
    nomeProduto = req_data['nomeProduto']
    descricaoProduto = req_data['descricaoProduto']
    valorUnitario = req_data['valorUnitario']
    quantidade = req_data['quantidade']
    quantidadeMinima = req_data['quantidadeMinima']

    produtos = Produtos()

    if(produtos.insertProduto(id_fornecedor, id_categoria, nomeProduto, descricaoProduto, valorUnitario, quantidade, quantidadeMinima)):
        result = {"result": "Dados inseridos com sucesso"}
    else:
        result = {"result": "Problemas para inserir os dados"}
    return jsonify(result)


@app.route('/insertCompra', methods=['POST'])
def insertCompra():
    if not request.json:
        abort(400)
    req_data = request.get_json()

    id_fornecedor = req_data['id_fornecedor']
    id_categoria = req_data['id_categoria']
    id_produto = req_data['id_produto']
    quantidade = req_data['quantidade']
    compras = Compras()
    produtos = Produtos()
    preco = produtos.getprecoByIdProduto(
        "where id_produto = " + str(id_produto))
    valorTotal = 0
    for p in preco:
        valorTotal += p * quantidade
    if(compras.insertCompra(id_fornecedor, id_produto, id_categoria, valorTotal, quantidade)):
        result = {"result": "Dados inseridos com sucesso"}
    else:
        result = {"result": "Problemas para inserir os dados"}
    return jsonify(result)


@app.route('/insertVenda', methods=['POST'])
def insertVenda():
    if not request.json:
        abort(400)
    req_data = request.get_json()

    id_vendedor = req_data['id_vendedor']
    id_categoria = req_data['id_categoria']
    id_produto = req_data['id_produto']
    quantidade = req_data['quantidade']
    vendas = Vendas()
    produtos = Produtos()
    preco = produtos.getprecoByIdProduto(
        "where id_produto = " + str(id_produto))
    valorTotal = 0
    taxaLucro = decimal.Decimal(0.8)

    for p in preco:
        valorTotal += (1 + taxaLucro) * p * quantidade
    if(vendas.insertVenda(id_vendedor, id_produto, id_categoria, valorTotal, quantidade)):
        result = {"result": "Dados inseridos com sucesso"}
    else:
        result = {"result": "Problemas para inserir os dados"}
    return jsonify(result)

### Fim metodos de insert

### Inicio metodos de consulta
#@app.route('/consultaVendedores', methods=['GET'])
#def consultaVendedor():
#    global vendedor
#    get_vendedor = Vendedor(None, None, None, None, None, None, )
#    get_vendedor.consultaVendedor()
#    res = {'status': 'ok', 'data': get_vendedor.listaVendedores}
#    return jsonify(res)

@app.route('/consultaVendedores', methods = ['GET'])
def consultavendedores():
    consultaVendedores =  []
    vendedor = Vendedores().consultaVendedores()
    for i in vendedor:
        f = {'id_vendedor': i[0], 'cpf': i[1], 'nome': i[2], 'carteiraTrabalho': i[3], 'telefone': i[4], 'dataAdmissao': i[5]}
        consultaVendedores.append(f)
    return jsonify(consultaVendedores)

@app.route('/consultaFornecedores', methods = ['GET'])
def consultafornecedores():
    consultafornecedor = []
    fornecedores = Fornecedores().consultaFornecedores()
    for i in fornecedores:
        f = {'id_fornecedor': i[0], 'cnpj': i[1], 'razaoSocial': i[2], 'telefone': i[3], 'endereco': i[4], 'contato': i[5]}
        consultafornecedor.append(f)
    return jsonify(consultafornecedor)

@app.route('/consultaCategorias', methods = ['GET'])
def consultacategorias():
    consultacategorias =  []
    categorias = Categorias().consultaCategorias()
    for i in categorias:
        f = {'id_categoria': i[0], 'tituloCategoria': i[1], 'descricaoCategoria': i[2]}
        consultacategorias.append(f)
    return jsonify(consultacategorias)

@app.route('/consultaProdutos', methods = ['GET'])
def consultaprodutos():
    consultaprodutos =  []
    produtos = Produtos().consultaProdutos()
    for i in produtos:
        f = {'id_categoria': i[0], 'tituloCategoria': i[1], 'descricaoCategoria': i[2]}
        consultaprodutos.append(f)
    return jsonify(consultaprodutos)

@app.route('/consultaCompras', methods = ['GET'])
def consultacompras():
    consultacompras =  []
    compras = Compras().consultaCompras()
    for i in compras:
        f = {'id_compra': i[0], 'id_fornecedor': i[1], 'id_produto': i[2], 'id_categoria': i[3],
        'dataCompra': i[4], 'valorTotal': float(i[5]), 'quantidade': i[6]}
        consultacompras.append(f)
    return jsonify(consultacompras)

@app.route('/consultaVendas', methods = ['GET'])
def consultavendas():
    consultavendas =  []
    vendas = Vendas().consultaVendas()
    for i in vendas:
        f = {'id_venda': i[0], 'id_vendedor': i[1], 'id_produto': i[2], 'id_categoria': i[3],
        'dataVenda': i[4], 'valorTotal': float(i[5]), 'quantidade': i[6]}
        consultavendas.append(f)
    return jsonify(consultavendas)

##### Fim metodos de consulta

### Inicio metodos de update
#@app.route('/updateVendedor', methods=['PUT'])
#def updateVendedor():
#    req_data = request.get_json()
#    print(req_data)
#    att_vendedor = Vendedores(None, None, None, None, None, None, )
#    att_vendedor.updateVendedor(req_data['cpf'], req_data['nome'], req_data['telefone'],
#                                req_data['carteiraTrabalho'], req_data['dataAdmissao'], req_data['fg_ativo'], req_data["id_vendedor"])
#    res = {'status': 'ok'}
#    return jsonify(res)
#
#### Fim metodos de update
#
#### Inicio metodos de delete
#@app.route('/deleteVendedor', methods=['DELETE'])
#def deleteVendedor():
#    global vendedor
#    req_data = request.get_json()
#    print(req_data)
#    del_vendedor = Vendedor(None, None, None, None, None, None, )
#    del_vendedor.deleteVendedor(req_data['id_vendedor'])
#    res = {'status': 'ok'}
#    return jsonify(res)
#
### Fim metodos de delete
