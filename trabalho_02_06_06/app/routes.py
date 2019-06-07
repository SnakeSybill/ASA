from flask import render_template
from flask import Flask, url_for, request, json, jsonify, abort
from json import dumps
from datetime import datetime
import decimal
from app import app

from models import Categorias, Fornecedores, Produtos, Compras, Vendas, Vendedores

#### Telas
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
    return render_template("fornecedores.html", consultafornecedores = [])

@app.route('/vendas')
def lista_vendas():
    return render_template("vendas.html", consultavendas = [])

@app.route('/vendedores')
def lista_vendedores():
    return render_template("vendedores.html", consultacategorias = [])

@app.route('/produtos')
def lista_produtos():
    return render_template("produtos.html", consultaprodutos = [])



#### Categorias - Testados
@app.route('/consultaCategorias/<nome>', methods = ['GET']) #### OK
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

@app.route('/consultaCategoriasAll', methods = ['GET']) #### OK
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

@app.route('/insertCategoria', methods=['POST']) #### OK
def insertCategoria():
    if not request.json:
        abort(400)
    req_data = request.get_json()
    categoria = Categorias()
    categoria.titulocategoria = req_data['titulocategoria']
    categoria.descricaocategoria = req_data['descricaocategoria']
    categoria.fg_ativo = req_data['fg_ativo']
    if(categoria.insertCategoria()):
        result = {"result": "Dados inseridos com sucesso"}
    else:
        result = {"result": "Problemas para inserir os dados"}
    return jsonify(result)

@app.route('/updateCategoria', methods=['PUT']) #### OK
def updateCategoria():
    if not request.json:
        abort(400)
    req_data = request.get_json()
    print("REQDATA " % req_data)
    categoria = Categorias()
    categoria.titulocategoria = req_data['titulocategoria']
    categoria.descricaocategoria = req_data['descricaocategoria']
    categoria.fg_ativo =  req_data['fg_ativo']
    categoria.id_categoria = req_data['id_categoria']
    if(categoria.updateCategoria()):
        result = {"result": "Dados atualizados com sucesso"}
    else:
        result = {"result": "Problemas para atualizar os dados"}
    return jsonify(result)

@app.route('/deleteCategoria/<id>', methods=['DELETE']) #### OK
def deleteCategoria(id):
    categoriaParameters = Categorias()
    categoriaParameters.id_categoria = id
    consultaCategorias = categoriaParameters.deleteCategoria()
    return jsonify(consultaCategorias)



#### Fornecedores
@app.route('/consultaFornecedores/<razaosocial>', methods = ['GET']) #### OK
def consultafornecedores(razaosocial):
    consultaFornecedores =  []
    consultaFornecedoresReturn = []
    fornecedorParameters = Fornecedores()
    fornecedorParameters.razaosocial = razaosocial
    consultaFornecedores = fornecedorParameters.consultaFornecedores()
    for i in consultaFornecedores:
        f = {'id_fornecedor': i.id_fornecedor, 'cnpj': i.cnpj, 'razaosocial': i.razaosocial, "fg_ativo": i.fg_ativo, "telefone": i.telefone, "contato": i.contato, "endereco": i.endereco}
        consultaFornecedoresReturn.append(f)
    return jsonify(consultaFornecedoresReturn)

@app.route('/consultaFornecedoresAll', methods = ['GET']) #### OK
def consultafornecedoresAll():
    consultaFornecedores =  []
    consultaFornecedoresReturn = []
    fornecedorParameters = Fornecedores()
    consultaFornecedores = fornecedorParameters.consultaFornecedoresAll()
    for i in consultaFornecedores:
        f = {'id_fornecedor': i.id_fornecedor, 'cnpj': i.cnpj, 'razaosocial': i.razaosocial, "fg_ativo": i.fg_ativo, "telefone": i.telefone, "contato": i.contato, "endereco": i.endereco}
        consultaFornecedoresReturn.append(f)
    return jsonify(consultaFornecedoresReturn)

@app.route('/insertFornecedor', methods=['POST']) #### OK
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

@app.route('/updateFornecedor', methods=['PUT']) #### OK
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

@app.route('/deleteFornecedor/<id>', methods=['DELETE']) #### OK
def deleteFornecedor(id):
    fornecedorParameters = Fornecedores()
    fornecedorParameters.id_fornecedor = id
    consultaFornecedores = fornecedorParameters.deleteFornecedor()
    return jsonify(consultaFornecedores)



#### Produtos
@app.route('/consultaProdutos/<nomeproduto>', methods = ['GET']) #### OK
def consultaprodutos(nomeproduto):
    consultaProdutos =  []
    consultaProdutosReturn = []
    produtoParameters = Produtos()
    produtoParameters.nomeproduto = nomeproduto
    consultaProdutos = produtoParameters.consultaProdutos()
    for i in consultaProdutos:
        f = {
                'id_produto': i[0].id_produto, 
                'nomeproduto': i[0].nomeproduto, 
                'descricaoproduto': i[0].descricaoproduto, 
                "fg_ativo": i[0].fg_ativo, 
                "categoria": {
                                "id_categoria": i[0].id_categoria, 
                                "titulocategoria": i[1].titulocategoria
                             },
                "valorunitario": str(i[0].valorunitario), 
                "quantidade": i[0].quantidade, 
                "quantidademinima": i[0].quantidademinima
            }
        consultaProdutosReturn.append(f)
    return jsonify(consultaProdutosReturn)

@app.route('/consultaProdutosAll', methods = ['GET']) #### OK
def consultaprodutosAll():
    consultaProdutos =  []
    consultaProdutosReturn = []
    produtoParameters = Produtos()
    consultaProdutos = produtoParameters.consultaProdutosAll()
    for i in consultaProdutos:
        f = {
                'id_produto': i[0].id_produto, 
                'nomeproduto': i[0].nomeproduto, 
                'descricaoproduto': i[0].descricaoproduto, 
                "fg_ativo": i[0].fg_ativo, 
                "categoria": {
                                "id_categoria": i[0].id_categoria, 
                                "titulocategoria": i[1].titulocategoria
                             },
                "valorunitario": str(i[0].valorunitario), 
                "quantidade": i[0].quantidade, 
                "quantidademinima": i[0].quantidademinima
            }
        consultaProdutosReturn.append(f)
    return jsonify(consultaProdutosReturn)

@app.route('/insertProduto', methods=['POST']) #### OK
def insertProduto():
    if not request.json:
        abort(400)
    req_data = request.get_json()
    produto = Produtos()
    produto.nomeproduto = req_data['nomeproduto']
    produto.descricaoproduto = req_data['descricaoproduto']
    produto.fg_ativo = req_data['fg_ativo']
    produto.id_fornecedor = req_data['id_fornecedor']
    produto.id_categoria = req_data['id_categoria']
    produto.valorunitario = req_data['valorunitario']
    produto.quantidade = req_data['quantidade']
    produto.quantidademinima = req_data['quantidademinima']

    if(produto.insertProduto()):
        result = {"result": "Dados inseridos com sucesso"}
    else:
        result = {"result": "Problemas para inserir os dados"}
    return jsonify(result)

@app.route('/updateProduto', methods=['PUT']) #### OK
def updateProduto():
    if not request.json:
        abort(400)
    req_data = request.get_json()
    produto = Produtos()
    produto.id_produto = req_data['id_produto']
    produto.nomeproduto = req_data['nomeproduto']
    produto.descricaoproduto = req_data['descricaoproduto']
    produto.fg_ativo = req_data['fg_ativo']
    produto.id_fornecedor = req_data['id_fornecedor']
    produto.id_categoria = req_data['id_categoria']
    produto.valorunitario = req_data['valorunitario']
    produto.quantidade = req_data['quantidade']
    produto.quantidademinima = req_data['quantidademinima']
    
    if(produto.updateProduto()):
        result = {"result": "Dados atualizados com sucesso"}
    else:
        result = {"result": "Problemas para atualizar os dados"}
    return jsonify(result)

@app.route('/deleteProduto/<id>', methods=['DELETE']) #### OK
def deleteProduto(id):
    produtoParameters = Produtos()
    produtoParameters.id_produto = id
    consultaProdutos = produtoParameters.deleteProduto()
    return jsonify(consultaProdutos)



#### Vendedores
@app.route('/consultaVendedores/<nome>', methods = ['GET']) #### OK
def consultavendedores(nome):
    consultaVendedores =  []
    consultaVendedoresReturn = []
    vendedorParameters = Vendedores()
    vendedorParameters.nome = nome
    consultaVendedores = vendedorParameters.consultaVendedores()
    for i in consultaVendedores:
        f = {'id_vendedor': i.id_vendedor, 'cpf': i.cpf, 'nome': i.nome, "fg_ativo": i.fg_ativo, "telefone": i.telefone, "carteiratrabalho": i.carteiratrabalho, "dataadmissao": i.dataadmissao}
        consultaVendedoresReturn.append(f)
    return jsonify(consultaVendedoresReturn)

@app.route('/consultaVendedoresAll', methods = ['GET']) #### OK
def consultavendedoresAll():
    consultaVendedores =  []
    consultaVendedoresReturn = []
    vendedorParameters = Vendedores()
    consultaVendedores = vendedorParameters.consultaVendedoresAll()
    for i in consultaVendedores:
        f = {'id_vendedor': i.id_vendedor, 'cpf': i.cpf, 'nome': i.nome, "fg_ativo": i.fg_ativo, "telefone": i.telefone, "carteiratrabalho": i.carteiratrabalho, "dataadmissao": i.dataadmissao}
        consultaVendedoresReturn.append(f)
    return jsonify(consultaVendedoresReturn)

@app.route('/insertVendedor', methods=['POST']) #### OK
def insertVendedor():
    if not request.json:
        abort(400)
    req_data = request.get_json()
    vendedor = Vendedores()
    vendedor.cpf = req_data['cpf']
    vendedor.nome = req_data['nome']
    vendedor.telefone = req_data['telefone']
    vendedor.carteiratrabalho = req_data['carteiratrabalho']
    vendedor.dataadmissao = req_data['dataadmissao']
    vendedor.fg_ativo = req_data['fg_ativo']

    if(vendedor.insertVendedor()):
        result = {"result": "Dados inseridos com sucesso"}
    else:
        result = {"result": "Problemas para inserir os dados"}
    return jsonify(result)

@app.route('/updateVendedor', methods=['PUT']) #### OK
def updateVendedor():
    if not request.json:
        abort(400)
    req_data = request.get_json()
    vendedor = Vendedores()
    vendedor.id_vendedor = req_data['id_vendedor']
    vendedor.cpf = req_data['cpf']
    vendedor.nome = req_data['nome']
    vendedor.telefone = req_data['telefone']
    vendedor.carteiratrabalho = req_data['carteiratrabalho']
    vendedor.dataadmissao = req_data['dataadmissao']
    vendedor.fg_ativo = req_data['fg_ativo']
    if(vendedor.updateVendedor()):
        result = {"result": "Dados atualizados com sucesso"}
    else:
        result = {"result": "Problemas para atualizar os dados"}
    return jsonify(result)

@app.route('/deleteVendedor/<id>', methods=['DELETE']) #### OK
def deleteVendedor(id):
    vendedorParameters = Vendedores()
    vendedorParameters.id_vendedor = id
    consultaVendedores = vendedorParameters.deleteVendedor()
    return jsonify(consultaVendedores)



#### Compras - Testados
@app.route('/consultaCompras/<idProduto>', methods = ['GET']) #### OK
def consultacompras(idProduto):
    consultaCompras =  []
    consultaComprasReturn = []
    compraParameters = Compras()
    compraParameters.id_produto = idProduto
    consultaCompras = compraParameters.consultaCompras()
    for i in consultaCompras:
        f = {
                'id_compra': i[0].id_compra, 
                'produto': {
                                'id_produto': i[0].id_produto, 
                                'nomeproduto': i[1].nomeproduto
                            }, 
                "fg_ativo": i[0].fg_ativo, 
                'fornecedor': {
                                    "id_fornecedor": i[0].id_fornecedor, 
                                    "razaosocial": i[2].razaosocial
                                },
                "datacompra": i[0].datacompra, 
                "valortotal": str(i[0].valortotal), 
                "quantidade": i[0].quantidade,
                'categoria': {
                                'id_categoria': i[0].id_categoria,
                                'titulocategoria': i[3].titulocategoria
                }
            }
        consultaComprasReturn.append(f)
    return jsonify(consultaComprasReturn)

@app.route('/consultaComprasAll', methods = ['GET']) #### OK
def consultacomprasAll():
    consultaCompras =  []
    consultaComprasReturn = []
    compraParameters = Compras()
    consultaCompras = compraParameters.consultaComprasAll()
    for i in consultaCompras:
        f = {
                'id_compra': i[0].id_compra, 
                'produto': {
                                'id_produto': i[0].id_produto, 
                                'nomeproduto': i[1].nomeproduto
                            }, 
                "fg_ativo": i[0].fg_ativo, 
                'fornecedor': {
                                    "id_fornecedor": i[0].id_fornecedor, 
                                    "razaosocial": i[2].razaosocial
                                },
                "datacompra": i[0].datacompra, 
                "valortotal": str(i[0].valortotal), 
                "quantidade": i[0].quantidade,
                'categoria': {
                                'id_categoria': i[0].id_categoria,
                                'titulocategoria': i[3].titulocategoria
                }
            }
        consultaComprasReturn.append(f)
    return jsonify(consultaComprasReturn)

@app.route('/insertCompra', methods=['POST']) #### OK
def insertCompra():
    if not request.json:
        abort(400)
    req_data = request.get_json()
    compra = Compras()
    compra.id_categoria = req_data['id_categoria']
    compra.id_produto = req_data['id_produto']
    compra.id_fornecedor = req_data['id_fornecedor']
    compra.datacompra = req_data['datacompra']
    compra.valortotal = req_data['valortotal']
    compra.quantidade = req_data['quantidade']
    compra.fg_ativo = req_data['fg_ativo']
    if(compra.insertCompra()):
        result = {"result": "Dados inseridos com sucesso"}
    else:
        result = {"result": "Problemas para inserir os dados"}
    return jsonify(result)

@app.route('/updateCompra', methods=['PUT']) #### OK
def updateCompra():
    if not request.json:
        abort(400)
    req_data = request.get_json()
    print("REQDATA " % req_data)
    compra = Compras()
    compra.id_categoria = req_data['id_categoria']
    compra.id_produto = req_data['id_produto']
    compra.id_fornecedor = req_data['id_fornecedor']
    compra.datacompra = req_data['datacompra']
    compra.valortotal = req_data['valortotal']
    compra.quantidade = req_data['quantidade']
    compra.id_compra = req_data['id_compra']
    if(compra.updateCompra()):
        result = {"result": "Dados atualizados com sucesso"}
    else:
        result = {"result": "Problemas para atualizar os dados"}
    return jsonify(result)

@app.route('/deleteCompra/<id>', methods=['DELETE'])
def deleteCompra(id):
    compraParameters = Compras()
    compraParameters.id_compra = id
    consultaCompras = compraParameters.deleteCompra()
    return jsonify(consultaCompras)



#### Vendas
@app.route('/consultaVendas/<idProduto>', methods = ['GET']) #### OK
def consultavendas(idProduto):
    consultaVendas =  []
    consultaVendasReturn = []
    vendaParameters = Vendas()
    vendaParameters.id_produto = idProduto
    consultaVendas = vendaParameters.consultaVendas()
    for i in consultaVendas:
        f = {
                'id_venda': i[0].id_venda, 
                'produto': {
                                'id_produto': i[0].id_produto, 
                                'nomeproduto': i[1].nomeproduto
                            }, 
                "fg_ativo": i[0].fg_ativo, 
                'vendedor': {
                                    "id_vendedor": i[0].id_vendedor, 
                                    "nome": i[2].nome
                                },
                "datavenda": i[0].datavenda, 
                "valortotal": str(i[0].valortotal), 
                "quantidade": i[0].quantidade,
                'categoria': {
                                'id_categoria': i[0].id_categoria,
                                'titulocategoria': i[3].titulocategoria
                }
            }
        consultaVendasReturn.append(f)
    return jsonify(consultaVendasReturn)

@app.route('/consultaVendasAll', methods = ['GET']) #### OK
def consultavendasAll():
    consultaVendas =  []
    consultaVendasReturn = []
    vendaParameters = Vendas()
    consultaVendas = vendaParameters.consultaVendasAll()
    for i in consultaVendas:
        f = {
                'id_venda': i[0].id_venda, 
                'produto': {
                                'id_produto': i[0].id_produto, 
                                'nomeproduto': i[1].nomeproduto
                            }, 
                "fg_ativo": i[0].fg_ativo, 
                'vendedor': {
                                    "id_vendedor": i[0].id_vendedor, 
                                    "nome": i[2].nome
                                },
                "datavenda": i[0].datavenda, 
                "valortotal": str(i[0].valortotal), 
                "quantidade": i[0].quantidade,
                'categoria': {
                                'id_categoria': i[0].id_categoria,
                                'titulocategoria': i[3].titulocategoria
                }
            }
        consultaVendasReturn.append(f)
    return jsonify(consultaVendasReturn)

@app.route('/insertVenda', methods=['POST']) #### OK
def insertVenda():
    if not request.json:
        abort(400)
    req_data = request.get_json()
    venda = Vendas()
    venda.id_categoria = req_data['id_categoria']
    venda.id_produto = req_data['id_produto']
    venda.id_vendedor = req_data['id_vendedor']
    venda.datavenda = req_data['datavenda']
    venda.valortotal = req_data['valortotal']
    venda.quantidade = req_data['quantidade']
    venda.fg_ativo = req_data['fg_ativo']
    if(venda.insertVenda()):
        result = {"result": "Dados inseridos com sucesso"}
    else:
        result = {"result": "Problemas para inserir os dados"}
    return jsonify(result)

@app.route('/updateVenda', methods=['PUT']) #### OK
def updateVenda():
    if not request.json:
        abort(400)
    req_data = request.get_json()
    print("REQDATA " % req_data)
    venda = Vendas()
    venda.id_categoria = req_data['id_categoria']
    venda.id_produto = req_data['id_produto']
    venda.id_vendedor = req_data['id_vendedor']
    venda.datavenda = req_data['datavenda']
    venda.valortotal = req_data['valortotal']
    venda.quantidade = req_data['quantidade']
    venda.id_venda = req_data['id_venda']
    if(venda.updateVenda()):
        result = {"result": "Dados atualizados com sucesso"}
    else:
        result = {"result": "Problemas para atualizar os dados"}
    return jsonify(result)

@app.route('/deleteVenda/<id>', methods=['DELETE']) #### OK
def deleteVenda(id):
    vendaParameters = Vendas()
    vendaParameters.id_venda = id
    consultaVendas = vendaParameters.deleteVenda()
    return jsonify(consultaVendas)

#### Erros
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404