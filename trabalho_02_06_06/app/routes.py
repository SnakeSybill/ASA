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

@app.route('/consultaCategorias/<nome>/<ativa>/<inativa>', methods = ['GET'])
def consultacategorias(nome, ativa, inativa):
    consultacategorias =  []
    categorias = Categorias().consultaCategorias()
    for i in categorias:
        f = {'id_categoria': i[0], 'tituloCategoria': i[1], 'descricaoCategoria': i[2]}
        consultacategorias.append(f)
    print(nome, ativa, inativa)
    print(consultacategorias)
    return jsonify(consultacategorias)

@app.route('/insertCategoria', methods=['POST'])
def insertCategoria():
    print("request")
    print(request)
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

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
