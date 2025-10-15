from abc import ABCMeta, abstractmethod


# Interface

class Carteira(metaclass=ABCMeta):
    @abstractmethod
    def pagar(self):
        pass



#object real

class Banco(Carteira):

    def __init__(self):
        self.cartao = None
        self.conta = None


    def __get_conta(self):
            self.conta = self.cartao

            return self.conta
        
    def __tem_saldo(self):
            print(f' Banco:: Checando se a conta {self.__get_conta()} tem saldo')

            return True
        
    def _set_cartao(self, cartao):
            self.cartao = cartao


    def pagar(self):
            if self.__tem_saldo():
                print(f' Banco:: Pagando com a conta {self.__get_conta()}')
                return True
            else:
                print(f' Banco:: Conta {self.__get_conta()} sem saldo')
                return False
            

#proxy

class CartaoProxy(Carteira):
    def __init__(self):
       
        self.banco = Banco()


    def pagar(self):
        cartao = input('Proxy: Insira o cartão: ')
        self.banco._set_cartao(cartao)

        return self.banco.pagar()
    

class Cliente:
    def __init__(self):
        print('Cliente: Criando o cartão')
        self.cartao = CartaoProxy()
        self.comprei = None

    def comprar(self):
        self.comprei = self.cartao.pagar()


    def __del__(self):
        if self.comprei:
            print('Cliente: Comprei')
        else:
            print('Cliente: Nao comprei')



if __name__ == '__main__':
    cliente = Cliente()
    cliente.comprar()