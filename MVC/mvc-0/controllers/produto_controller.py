from tornado.web import RequestHandler
from models.produto_model import ProdutoModel


class index(RequestHandler):
    def get(self):
        produtos = ProdutoModel.get_produtos()
        self.render("index.html", produtos=produtos)


class Novo(RequestHandler):
    def get(self):
        self.render("novo.html")

    def post(self):
        nome = self.get_argument("nome", None)
        preco = self.get_argument("preco", None)
        produto = ProdutoModel(nome=nome, preco=preco)

        produto.salvar()
        self.redirect("/")


class Atualizar(RequestHandler):

    def get(self, id, status):
        produto = ProdutoModel.get_produto(id)
        if not produto:
            self.redirect("/")
            return

        produto.status = int(status)
        produto.atualizar()

        self.redirect("/")


class Delete(RequestHandler):
    def get(self, id):
        produto = ProdutoModel.get_produto(id)
        if produto:
            produto.delet()
        self.redirect("/")
