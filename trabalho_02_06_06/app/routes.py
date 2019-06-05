from flask import render_template
from flask import Flask, url_for, request, json, jsonify, abort
from json import dumps
from datetime import datetime
import decimal
from app import app

from models import Categorias, Fornecedores, Produtos


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/categorias')
def lista_categorias():
    return render_template("categorias.html", consultacategorias = [])

@app.route('/compras')
def lista_compras():
    return render_template("compras.html", consultacompras = [])

@app.route('/fornecedores')
def lista_fornecedores():
    return render_template("categorias.html", consultacategorias = [])

@app.route('/produtos')
def lista_produtos():
    return render_template("categorias.html", consultacategorias = [])

@app.route('/consultaCategorias/<nome>', methods = ['GET'])
def consultacategorias(nome):
    consultaCategorias =  []
    consultaCategoriasReturn = []
    categoriaParameters = Categorias()
    categoriaParameters.titulocategoria = nome
    consultaCategorias = categoriaParameters.consultaCategorias()
    for i in consultaCategorias:
        f = {'id_categoria': i.id_categoria, 'titulocategoria': i.titulocategoria, 'descricaocategoria': i.descricaocategoria, "fg_ativo": i.fg_ativo}
        print("Item: ")
        print(f)
        consultaCategoriasReturn.append(f)
    return jsonify(consultaCategoriasReturn)

@app.route('/consultaCategoriasAll', methods = ['GET'])
def consultacategoriasAll():
    consultaCategorias =  []
    consultaCategoriasReturn = []
    categoriaParameters = Categorias()
    consultaCategorias = categoriaParameters.consultaCategoriasAll()
    for i in consultaCategorias:
        f = {'id_categoria': i.id_categoria, 'titulocategoria': i.titulocategoria, 'descricaocategoria': i.descricaocategoria, "fg_ativo": i.fg_ativo}
        print("Item: ")
        print(f)
        consultaCategoriasReturn.append(f)
    return jsonify(consultaCategoriasReturn)

@app.route('/insertCategoria', methods=['POST'])
def insertCategoria():
    if not request.json:
        abort(400)
    req_data = request.get_json()
    categoria = Categorias()
    categoria.titulocategoria = req_data['titulocategoria']
    categoria.descricaocategoria = req_data['descricaocategoria']
    categoria.fg_ativo = req_data['ativa']
    if(categoria.insertCategoria()):
        result = {"result": "Dados inseridos com sucesso"}
    else:
        result = {"result": "Problemas para inserir os dados"}
    return jsonify(result)

@app.route('/updateCategoria', methods=['PUT'])
def updateCategoria():
    if not request.json:
        abort(400)
    req_data = request.get_json()
    print("REQDATA " % req_data)
    categoria = Categorias()
    categoria.titulocategoria = req_data['titulocategoria']
    categoria.descricaocategoria = req_data['descricaocategoria']
    categoria.fg_ativo =  req_data['ativa']
    categoria.id_categoria = req_data['id_categoria']
    if(categoria.updateCategoria()):
        result = {"result": "Dados atualizados com sucesso"}
    else:
        result = {"result": "Problemas para atualizar os dados"}
    return jsonify(result)

@app.route('/deleteCategoria/<id>', methods=['DELETE'])
def deleteCategoria(id):
    categoriaParameters = Categorias()
    categoriaParameters.id_categoria = id
    consultaCategorias = categoriaParameters.deleteCategoria()
    return jsonify(consultaCategorias)


#### Fornecedores
@app.route('/consultaFornecedores/<cnpj>', methods = ['GET'])
def consultafornecedores(cnpj):
    consultaFornecedores =  []
    consultaFornecedoresReturn = []
    fornecedorParameters = Fornecedores()
    fornecedorParameters.cnpj = cnpj
    consultaFornecedores = fornecedorParameters.consultaFornecedores()
    for i in consultaFornecedores:
        f = {'id_fornecedor': i.id_fornecedor, 'cnpj': i.cnpj, 'razaosocial': i.razaosocial, "fg_ativo": i.fg_ativo, "telefone": i.telefone, "contato": i.contato, "endereco": i.endereco}
        consultaFornecedoresReturn.append(f)
    return jsonify(consultaFornecedoresReturn)

@app.route('/consultaFornecedoresAll', methods = ['GET'])
def consultafornecedoresAll():
    consultaFornecedores =  []
    consultaFornecedoresReturn = []
    fornecedorParameters = Fornecedores()
    consultaFornecedores = fornecedorParameters.consultaFornecedoresAll()
    for i in consultaFornecedores:
        f = {'id_fornecedor': i.id_fornecedor, 'cnpj': i.cnpj, 'razaosocial': i.razaosocial, "fg_ativo": i.fg_ativo, "telefone": i.telefone, "contato": i.contato, "endereco": i.endereco}
        consultaFornecedoresReturn.append(f)
    return jsonify(consultaFornecedoresReturn)

@app.route('/insertFornecedor', methods=['POST'])
def insertFornecedor():
    if not request.json:
        abort(400)
    req_data = request.get_json()
    fornecedor = Fornecedores()
    fornecedor.cnpj = req_data['cnpj']
    fornecedor.razaosocial = req_data['razaosocial']
    fornecedor.telefone = req_data['telefone']
    fornecedor.contato = req_data['contato']
    fornecedor.endereco = req_data['endereco']
    fornecedor.fg_ativo = req_data['fg_ativo']

    if(fornecedor.insertFornecedor()):
        result = {"result": "Dados inseridos com sucesso"}
    else:
        result = {"result": "Problemas para inserir os dados"}
    return jsonify(result)

@app.route('/updateFornecedor', methods=['PUT'])
def updateFornecedor():
    if not request.json:
        abort(400)
    req_data = request.get_json()
    fornecedor = Fornecedores()
    fornecedor.id_fornecedor = req_data['id_fornecedor']
    fornecedor.cnpj = req_data['cnpj']
    fornecedor.razaosocial = req_data['razaosocial']
    fornecedor.telefone = req_data['telefone']
    fornecedor.contato = req_data['contato']
    fornecedor.endereco = req_data['endereco']
    fornecedor.fg_ativo = req_data['fg_ativo']
    if(fornecedor.updateFornecedor()):
        result = {"result": "Dados atualizados com sucesso"}
    else:
        result = {"result": "Problemas para atualizar os dados"}
    return jsonify(result)

@app.route('/deleteFornecedor/<id>', methods=['DELETE'])
def deleteFornecedor(id):
    fornecedorParameters = Fornecedores()
    fornecedorParameters.id_fornecedor = id
    consultaFornecedores = fornecedorParameters.deleteFornecedor()
    return jsonify(consultaFornecedores)


#### Produtos
@app.route('/consultaProdutos/<nomeproduto>', methods = ['GET'])
def consultaprodutos(nomeproduto):
    consultaProdutos =  []
    consultaProdutosReturn = []
    produtoParameters = Produtos()
    produtoParameters.nomeproduto = nomeproduto
    consultaProdutos = produtoParameters.consultaProdutos()
    for i in consultaProdutos:
        f = {'id_produto': i.id_produto, 'nomeproduto': i.nomeproduto, 'descricaoproduto': i.descricaoproduto, "fg_ativo": i.fg_ativo, "categoria": i.categoria, "valorunitario": i.valorunitario, "quantidade": i.quantidade, "quantidademinima": i.quantidademinima}
        consultaProdutosReturn.append(f)
    return jsonify(consultaProdutosReturn)

@app.route('/consultaProdutosAll', methods = ['GET'])
def consultaprodutosAll():
    consultaProdutos =  []
    consultaProdutosReturn = []
    produtoParameters = Produtos()
    consultaProdutos = produtoParameters.consultaProdutosAll()
    for i in consultaProdutos:
        f = {
                'id_produto': i.id_produto, 
                'nomeproduto': i.nomeproduto, 
                'descricaoproduto': i.descricaoproduto, 
                "fg_ativo": i.fg_ativo, 
                "categoria": i.categoria, 
                "valorunitario": i.valorunitario, 
                "quantidade": i.quantidade, 
                "quantidademinima": i.quantidademinima
            }
        consultaProdutosReturn.append(f)
    return jsonify(consultaProdutosReturn)

@app.route('/insertProduto', methods=['POST'])
def insertProduto():
    if not request.json:
        abort(400)
    req_data = request.get_json()
    produto = Produtos()
    produto.nomeproduto = req_data['i.nomeproduto'],
    produto.descricaoproduto = req_data['i.descricaoproduto'],
    produto.fg_ativo = req_data['i.fg_ativo'],
    produto.categoria = req_data['i.categoria'],
    produto.valorunitario = req_data['i.valorunitario'],
    produto.quantidade = req_data['i.quantidade'],
    produto.quantidademinima = req_data['i.quantidademinima']

    if(produto.insertProduto()):
        result = {"result": "Dados inseridos com sucesso"}
    else:
        result = {"result": "Problemas para inserir os dados"}
    return jsonify(result)

@app.route('/updateProduto', methods=['PUT'])
def updateProduto():
    if not request.json:
        abort(400)
    req_data = request.get_json()
    produto = Produtos()
    produto.id_produto = req_data['i.id_produto'],
    produto.nomeproduto = req_data['i.nomeproduto'],
    produto.descricaoproduto = req_data['i.descricaoproduto'],
    produto.fg_ativo = req_data['i.fg_ativo'],
    produto.categoria = req_data['i.categoria'],
    produto.valorunitario = req_data['i.valorunitario'],
    produto.quantidade = req_data['i.quantidade'],
    produto.quantidademinima = req_data['i.quantidademinima']
    
    if(produto.updateProduto()):
        result = {"result": "Dados atualizados com sucesso"}
    else:
        result = {"result": "Problemas para atualizar os dados"}
    return jsonify(result)

@app.route('/deleteProduto/<id>', methods=['DELETE'])
def deleteProduto(id):
    produtoParameters = Produtos()
    produtoParameters.id_produto = id
    consultaProdutos = produtoParameters.deleteProduto()
    return jsonify(consultaProdutos)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
