from Model.Evento import Evento
class EventoDao():
    def __init__(self):
        self.model = Evento

    def list_all(self):
        lista = []
        arquivo = open(r'C:\Users\900160\Documents\EventosApi\Tabela','r')
        for i in arquivo:
            linha = i.split(';')
            list = {linha[0], linha[1], linha[2], linha[3], linha[4]}
            lista.append(list)
        return print(lista[0])

a = EventoDao()
a.list_all()



