class Object:
    def __init__(self):
        self.observadores = []

    def __repr__(self):
        return '::Object::'


    def registrar(self, observador):
        self.observadores.append(observador)

    def notificar_todos(self, *args, **kwargs):
        for observador in self.observadores:
            observador.notificar(self, *args, **kwargs)



class Observador1:

    def __init__(self,objeto):
        objeto.registrar(self)
    
    def notificar(self, objeto, *args):
        print(f'O {type(self).__name__} recebeu uma notificação de {type(objeto).__name__}')


class Observador2:

    def __init__(self,objeto):
        objeto.registrar(self)
    
    def notificar(self, objeto, *args):
        print(f'O {type(self).__name__} recebeu uma {args[0]} de {(objeto)}')





if __name__ == '__main__':
    obj = Object()
    
    obs1 = Observador1(obj)
    obs2 = Observador2(obj)
    obj.notificar_todos('teste','testandi')