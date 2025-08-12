# Padrão de Projeto: Singleton

## Definição
O Singleton é um padrão de projeto criacional que garante que uma classe tenha **apenas uma instância** e fornece um ponto global de acesso a ela.

## Objetivo
Evitar a criação de múltiplas instâncias de uma mesma classe, especialmente quando essas instâncias compartilham um **estado global** ou consomem muitos recursos.

## Quando Usar
- Quando deve existir **apenas um objeto** de uma determinada classe no sistema.
- Quando se deseja um **ponto único de acesso** a um recurso (ex: conexão com banco de dados, logger, gerenciador de configuração).

## Estrutura

- **Classe Singleton**: contém um atributo estático que armazena a única instância.
- O **construtor é privado ou protegido** para impedir que outras classes instanciem diretamente.
- Um método público estático retorna a instância única (geralmente chamado `getInstance()` ou equivalente).

## Exemplo (Python)

```python
class Singleton:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(Singleton, cls).__new__(cls)
        return cls._instancia

# Teste
obj1 = Singleton()
obj2 = Singleton()

print(obj1 is obj2)  # True
