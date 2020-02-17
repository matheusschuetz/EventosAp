from Model.Evento import Evento
class EventoDao():
    def __init__(self):
        self.model = Evento

    def list_all(self):
        lista = []
        arquivo = open(r'C:\Users\900160\Documents\EventosApi\Tabela','r')
        for i in arquivo:
            lista.append(i)
        return print(lista)

a = EventoDao()
a.list_all()



