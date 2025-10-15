🧩 Design Pattern Proxy em Python
📘 O que é o Proxy Pattern?

O Proxy Pattern (ou Padrão Proxy) é um padrão estrutural que fornece um substituto ou intermediário para outro objeto, controlando o acesso a ele.
Em outras palavras, o proxy age como um “representante” de outro objeto — o objeto real — adicionando camadas de controle, segurança ou otimização sem modificar o comportamento original.

🧠 Quando usar

O padrão é útil quando você precisa:

Controlar o acesso a um objeto (ex: autenticação, permissões, cache).

Adicionar comportamento extra antes ou depois da chamada real.

Reduzir custos de criação ou uso de objetos pesados.

Executar ações remotas como se fossem locais (ex: acesso remoto, APIs).

⚙️ Estrutura básica
from abc import ABC, abstractmethod

# Interface comum
class Subject(ABC):
    @abstractmethod
    def request(self):
        pass

# Objeto real
class RealSubject(Subject):
    def request(self):
        print("Executando a operação no objeto real.")

# Proxy
class Proxy(Subject):
    def __init__(self, real_subject: RealSubject):
        self._real_subject = real_subject

    def request(self):
        if self._check_access():
            print("Proxy: verificando acesso antes da chamada...")
            self._real_subject.request()
            self._log_access()
        else:
            print("Proxy: acesso negado.")

    def _check_access(self):
        # Exemplo simples de controle
        return True

    def _log_access(self):
        print("Proxy: log de acesso registrado.")

🧩 Exemplo de uso
real = RealSubject()
proxy = Proxy(real)

proxy.request()


Saída:

Proxy: verificando acesso antes da chamada...
Executando a operação no objeto real.
Proxy: log de acesso registrado.

💡 Benefícios

Encapsula a complexidade do objeto real.

Adiciona funcionalidades sem alterar o código original.

Facilita o controle de acesso, cache e logging.

🚫 Possíveis desvantagens

Pode aumentar a complexidade do sistema.

Introduz camadas adicionais de indireção, o que pode impactar performance.

🔍 Exemplos de aplicação prática

Proxy de segurança → valida permissões antes de executar uma ação.

Proxy de cache → guarda resultados de chamadas caras.

Proxy remoto → representa objetos que estão em outro servidor.

Proxy virtual → adia a criação de objetos pesados até serem realmente usados.

🧾 Conclusão

O Proxy Pattern é uma poderosa ferramenta para controlar e estender o comportamento de objetos de forma elegante e desacoplada.
Ele é muito utilizado em sistemas distribuídos, frameworks de rede e até em ORM’s (como o SQLAlchemy), onde proxies são usados para lazy loading e gerenciamento de conexões.