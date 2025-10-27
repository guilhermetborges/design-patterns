from abc import ABCMeta, abstractmethod

class Comando(metaclass=ABCMeta):
    def __init__(self,recv):
        self.recv = recv
        print('fui criado')

    
    @abstractmethod
    def executar(self):
        pass


class ComandoConcreto(Comando):

    def __init__(self, recv):
        print('cheguei aq')

        self.recv = recv
    
    def executar(self):
        self.recv.acao()


class Receiver:
    print('primeiro')

    def acao(self):
       print('Ação do receiver')


class invoker:
    print('invoker criado')

    def comando(self,cmd):
        print('minha parte')
        self.cmd = cmd

    def executar(self):
        
        print('executou')
        self.cmd.executar()

if __name__ == '__main__':
    recv = Receiver()
    cmd = ComandoConcreto(recv)


    invoker = invoker()
    invoker.comando(cmd)
    invoker.executar()