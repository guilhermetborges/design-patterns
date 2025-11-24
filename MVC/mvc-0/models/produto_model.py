from db import _executar


class ProdutoModel:
    def __init__(self, nome, preco, id=None, status=1):
        self.id = id   
        self.nome = nome
        self.preco = preco
        self.status = status
        self._ensure_table()

    @staticmethod
    def _ensure_table():
        query = """
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            status INTEGER DEFAULT 1
        );
        """
        _executar(query)

    def salvar(self):
        query = "INSERT INTO produtos (nome, preco, status) VALUES (?, ?, ?)"
        _executar(query, (self.nome, float(self.preco), self.status))

    def atualizar(self):
        query = "UPDATE produtos SET status=? WHERE id=?"
        _executar(query, (self.status, int(self.id)))

    def delet(self):
        query = "DELETE FROM produtos WHERE id=?"
        _executar(query, (int(self.id),))

    @staticmethod
    def _rows_to_dicts(produtos):
        if produtos and isinstance(produtos[0], dict):
            return produtos
        return [
            {"id": prod[0], "nome": prod[1], "preco": prod[2], "status": prod[3]}
            for prod in produtos
        ]

    @staticmethod
    def get_produtos():
        ProdutoModel._ensure_table()
        query = "SELECT id, nome, preco, status FROM produtos"
        produtos = _executar(query)
        return ProdutoModel._rows_to_dicts(produtos)

    @staticmethod
    def get_produto(id):
        ProdutoModel._ensure_table()
        query = "SELECT id, nome, preco, status FROM produtos WHERE id=?"
        resultado = _executar(query, (int(id),))
        if not resultado:
            return None
        produto = ProdutoModel._rows_to_dicts(resultado)[0]
        return ProdutoModel(
            nome=produto["nome"],
            preco=produto["preco"],
            id=produto["id"],
            status=produto["status"],
        )
