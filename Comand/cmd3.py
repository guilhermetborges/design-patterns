from abc import ABCMeta, abstractmethod

class Ordem(metaclass=ABCMeta):

    @abstractmethod
    def executar(self):
        pass


class OrdemComprar(Ordem):
    def __init__(self,acao):
        self.acao = acao


    def verificar(self):
        self.valor = ValorPedido.verificaValor_compra(self)

        return self.valor

    def executar(self):
        valor = self.verificar()
        print(f"valor: {valor}!")
        self.acao.comprar(valor)



class OrdemVenda(Ordem):
    def __init__(self,acao):
        self.acao = acao

    def verificar(self):
        self.valor = ValorPedido.verificaValor_venda(self)

        return self.valor
 

    def executar(self):
        valor = self.verificar()
        print(f"ação vendida por {valor}")
        self.acao.vender(valor)


class ValorPedido:
    def verificaValor_venda(self):
        self.valor = int(input("qual o valor necessario para vender essa ação: "))
        return self.valor
    
    def verificaValor_compra(self):
        self.valor = int(input("qual o valor necessario para comprar essa ação: "))
        return self.valor
    
#Receiver
class Acao:

    def comprar(self,valor):
        print(f"acao comprada no valor: {valor}")

    def vender(self,valor):
        print(f"voce vendeu a acao por {valor}")

    
#Invoker
class Agente:
    def __init__(self):
        self.__fila_ordens = []

    def adicionar_ordem_na_fila(self,ordem):
        self.__fila_ordens.append(ordem)
        ordem.executar()


if __name__ == '__main__':
    acao = Acao()

    ordem_compra = OrdemComprar(acao)

    ordem_venda = OrdemVenda(acao)

    agente = Agente()

    agente.adicionar_ordem_na_fila(ordem_compra)
    agente.adicionar_ordem_na_fila(ordem_venda)

