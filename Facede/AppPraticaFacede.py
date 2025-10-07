class GerenciamentodEmpleados:
    def __init__(self):
        print('gerencia de eventos')

    def organizar(self):
        self.salao = Salao()
        self.salao.agendar()

        self.florista = Florista()
        self.florista.fazer()

        self.restaurante = Restaurante()
        self.restaurante.preparar()






class Restaurante:
    def __init__(self):
        print('chamando garçom')
        

    def preparar(self):
        print('preparando comida')



class Florista:
    def __init__(self):
        print('chamando florista')

    def fazer(self):
        print('fazendo flores')



class Salao:
    def __init__(self):
        print

    

    def agendar(self):
        print('agendando evento')




if __name__ == '__main__':
    print('gerenciamento de eventos')
    gerenciamento = GerenciamentodEmpleados()
    gerenciamento.organizar()
