from flask import render_template
from flask import Flask, url_for, request, json, jsonify, abort
from json import dumps
from datetime import datetime
import decimal
from app import app

from categorias import Categorias

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/categorias')
def lista_disciplinas():
    return render_template("categorias.html", consultacategorias = [])

@app.route('/consultaCategorias/<nome>', methods = ['GET'])
def consultacategorias(nome):
    consultaCategorias =  []
    consultaCategoriasReturn = []
    categoriaParameters = Categorias()
    categoriaParameters.titulocategoria = nome
    #categoriaParameters.fg_ativo = ativa
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

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
