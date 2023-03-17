from flask_restful import Resource
from flask import request
import json

habilidades = ['Python', 'Java', "Flask", ".NET"]

class ListaHabilidades(Resource):
    def get(self):
        return habilidades
    
    def post(self):
        dados = json.loads(request.data)
        for hab in dados['habilidades']:
            habilidades.append(hab)
        return habilidades
    
class Habilidades(Resource):
    def get(self, position):
        return habilidades[position]
    
    def put(self, position):
        dados = json.loads(request.data)
        habilidades[position] = dados['name']
        return habilidades
    
    def delete(self, position):
        habilidades.pop(position)
        return {"status":"Sucesso", "mensagem":"Registro Excluido"}