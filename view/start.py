from flask import Flask
from flask_restful import Api

from Controller.Evento_controller import EventoController
from

app = Flask(__name__)
api = Api(app)

api.add_resource(EventoController, '/api/evento', endpoint='evento')

@app.route('/')

def start():
    return 'tste'

app.run(debug=True)