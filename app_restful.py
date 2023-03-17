from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import ListaHabilidades, Habilidades
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
    "id":"0",
    "nome":"Ademir",
    "habilidades":["Python", "Api"]
    },
    {
    "id":"1",
    "nome":"Monteiro",
    "habilidades":["Java", ".NET"]
    }
]

# Buscar um desenvolvedor pelo ID, também altera e deleta um desenvolvedor
class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = f"Desenvolvedor de ID {id} não existe"
            response = {"status":"erro", "mensagem":mensagem}
        except Exception:
            mensagem = "Erro desconhecido. Procure o adm da API"
            response = {"status":"erro", "mensagem":mensagem}

        return response
    
    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {"status":"Sucesso", "mensagem":"Registro Excluido"}

# Lista todos os desenvolvedores e permite registrar um novo desenvolvedor
class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores
    
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]
         
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Desenvolvedor, '/dev/<int:id>')
api.add_resource(ListaHabilidades, '/habilidades/')
api.add_resource(Habilidades, '/habilidades/<int:position>')

if __name__ == "__main__":
    app.run(debug = True)