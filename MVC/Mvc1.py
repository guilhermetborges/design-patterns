class Model:
    def __init__(self):
        self.produtos = {
            'ps5': { 'id': 1, 'nome': 'Playstation 5', 'preco': 5000 },
            'xbox': { 'id': 2, 'nome': 'Xbox Series X', 'preco': 4000 },
            'ipad': { 'id': 3, 'nome': 'iPad', 'preco': 3000 }
        }


class Controller:
    def __init__(self):
        self.model = Model()


    def get_produtos(self):
        produtos = self.model.produtos.keys()
         
        for chave in produtos:
            print(f"{self.model.produtos[chave]['id']} - {self.model.produtos[chave]['nome']} - {self.model.produtos[chave]['preco']}")


class View:
    def __init__(self):
        self.controller = Controller()
        
    def Produtos(self):
        self.controller.get_produtos()


if __name__ == '__main__':
    view = View()
    view.Produtos()