
def list_all()
    lista = []
    arquivo = open(r"C:\Users\900152\Documents\EventosApi\Tabela", "r")
    for i in arquivo:
        lista.append(i)
    print(lista)