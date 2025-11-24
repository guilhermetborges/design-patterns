🛠️ Padrão Template Method em Python: O Esqueleto Algorítmico

O Template Method é um Padrão de Projeto Comportamental que define o esqueleto de um algoritmo em uma superclasse abstrata, mas delega a implementação de passos específicos para as subclasses. 
Em essência, ele assegura que a estrutura e a sequência de um processo permaneçam fixas, enquanto permite a variação controlada de certas etapas.

🧠 Quando UsarO Padrão Template Method é útil quando você precisa:Reutilizar Código Comum: Centralizar as partes imutáveis de um algoritmo na classe base, evitando duplicação de código (Princípio DRY).
Controlar a Estrutura: Impor uma ordem de execução fixa para uma série de passos, garantindo que o algoritmo siga a sequência correta.
Permitir Extensão Controlada: Fornecer aos frameworks e bibliotecas um mecanismo onde os desenvolvedores podem estender funcionalidades implementando apenas os métodos variáveis (Princípio Open/Closed).

⚙️ Estrutura e Exemplo BásicoA estrutura envolve uma Classe Abstrata que contém o Template Method (o método principal) e métodos abstratos ou concretos chamados de primitivas ou hooks (ganchos). As Subclasses Concretas implementam as primitivas variáveis.


Python

from abc import ABC, abstractmethod

# 1. Classe Abstrata (Define o Template Method)
class PreparaBebida(ABC):
    def preparar_receita(self):
        """O Template Method: Esqueleto do algoritmo."""
        self.ferver_agua() # Passo Concreto
        self.adicionar_ingrediente_principal() # Passo Abstrato
        self.despejar_no_copo()
        self.adicionar_condimentos() # Passo Abstrato

    def ferver_agua(self):
        print("1. Fervendo a água...")

    def despejar_no_copo(self):
        print("3. Despejando no copo.")

    @abstractmethod
    def adicionar_ingrediente_principal(self):
        pass

    @abstractmethod
    def adicionar_condimentos(self):
        pass

# 2. Subclasse Concreta (Implementa os passos variáveis)
class Cafe(PreparaBebida):
    def adicionar_ingrediente_principal(self):
        print("2. Adicionando pó de Café.")

    def adicionar_condimentos(self):
        print("4. Adicionando açúcar e leite.")

# Exemplo de Uso
print("--- Preparando Café ---")
cafe = Cafe()
cafe.preparar_receita()
Saída:--- Preparando Café ---
1. Fervendo a água...
2. Adicionando pó de Café.
3. Despejando no copo.
4. Adicionando açúcar e leite.


💡 Benefícios e Desvantagens
✅ Benefícios:
Reutilização: Elimina código duplicado, centralizando a lógica comum na superclasse.Acoplamento Forte: Baseado em herança, a classe base e as subclasses ficam rigidamente acopladas.
Consistência: Garante que a sequência correta do algoritmo seja sempre executada.
Fácil Extensão: O cliente precisa implementar apenas os métodos variáveis para criar novas variantes.

🚫 Possíveis Desvantagens
Rígido: Se a variação exigir uma mudança na sequência do algoritmo, o padrão falha e deve ser substituído pelo padrão Strategy.

Violação LSP: Se o Template Method for muito longo, pode-se violar o Princípio de Substituição de Liskov se as subclasses não implementarem todos os passos de forma coerente.


🔍 Exemplos de Aplicação PráticaO Template Method é onipresente em frameworks:Processamento de Dados: Em bibliotecas de ETL (Extract, Transform, Load), onde a sequência (conexão, leitura, escrita) é fixa, mas a "Transformação" (T) é delegada ao usuário.Frameworks de UI: Define a sequência de desenho de um componente gráfico (montar, desenhar fundo, desenhar borda), permitindo que o desenvolvedor personalize o "desenhar conteúdo" específico.Algoritmos de Construção: Define a ordem de montagem de um produto, permitindo variação nas etapas de submontagem.🧾 ConclusãoO Template Method é uma solução elegante para a reutilização de código e a manutenção da integridade estrutural de um algoritmo. Ele controla o como e o quando as etapas fixas e variáveis são executadas, sendo um pilar na arquitetura de muitos frameworks extensíveis.