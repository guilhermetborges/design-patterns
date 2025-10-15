class Ator:

    def __init__(self):
        self.ocupado = False

    def indisponivel(self):
        self.ocupado = True
        print(f'{type(self).__name__} indisponivel')


    def disponivel(self):
        self.ocupado = False
        print(f'{type(self).__name__} está disponivel')

    def ver_disponobilidade(self):
        return self.ocupado
    


class Agente: #proxy
    def trabalho(self):
        ator = Ator()
        if ator.ver_disponobilidade():
            ator.indisponivel()
        else:
            ator.disponivel()



if __name__ == '__main__':
    agente = Agente()
    agente.trabalho()