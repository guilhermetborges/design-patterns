from abc import ABC, abstractmethod, ABCMeta

# Seções
class Secao(metaclass=ABCMeta):
    @abstractmethod
    def __repr__(self):
        pass

class SecaoPessoal(Secao):
    def __init__(self, *args, **kwargs):
        self.nome = 'Seção Pessoal'   

    def __repr__(self):
        return self.nome

    

class SecaoProjeto(Secao):
    def __repr__(self):
        return 'Seção Projeto'

class SecaoAlbum(Secao):
    def __repr__(self):
        return 'Seção Álbum'

# Perfil base
class Perfil(ABC):
    def __init__(self, nome):
        self.nome = nome
        self.secoes = []
        self.criar_perfil()

    @abstractmethod
    def criar_perfil(self):
        pass

    def get_secoes(self):
        return self.secoes

    def add_secao(self, secao):
        self.secoes.append(secao)

# Perfis específicos
class Linkedin(Perfil):
    def criar_perfil(self):
        self.add_secao(SecaoPessoal())
        self.add_secao(SecaoProjeto())
        self.add_secao(SecaoAlbum())

class Facebook(Perfil):
    def criar_perfil(self):
        self.add_secao(SecaoPessoal())
        self.add_secao(SecaoAlbum())

# Execução principal
if __name__ == '__main__':
    rede = input('Qual rede social você deseja (Linkedin/Facebook)?\n').strip()
    nome = input('Qual o nome do usuário do perfil?\n').strip()

    # Proteção contra eval inseguro
    redes = {
        'Linkedin': Linkedin,
        'Facebook': Facebook
    }

    perfil_cls = redes.get(rede)
    if perfil_cls:
        perfil = perfil_cls(nome)
        print(f'\nPerfil de {perfil.nome} criado com {len(perfil.get_secoes())} seções:')
        for secao in perfil.get_secoes():
            print('-', secao)
        print('\nDados internos:', perfil.__dict__)
    else:
        print('Rede social inválida.')
