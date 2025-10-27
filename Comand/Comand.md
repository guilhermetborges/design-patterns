🤖 Padrão de Projeto Command em Python: Encapsulando Ações
O Padrão Command (Comando) é um padrão comportamental que promove o desacoplamento extremo ao encapsular uma requisição (uma chamada de método) como um objeto de primeira classe. Em Python, o uso de classes abstratas e Type Hinting (sugestão de tipo) torna a implementação robusta e aderente ao Clean Code.

Para demonstrar, usaremos o exemplo clássico de um controle remoto universal controlando diferentes dispositivos.

🏗️ Componentes do Padrão em Python
Usaremos o módulo abc (Abstract Base Classes) para definir a interface (o contrato) do Comando.

1. Comando (Interface)
Define o contrato que todos os comandos concretos devem seguir.

Python

from abc import ABC, abstractmethod

# 1. Comando (Interface) - Define o contrato
class Comando(ABC):
    """
    Declara a interface para a execução de uma operação.
    """
    @abstractmethod
    def executar(self) -> None:
        pass
2. Receptor (Receiver)
O Receptor é o objeto que conhece e contém a lógica de negócios para executar a ação.

Python

# 2. Receptor (Receiver) - Contém a lógica de negócios
class Luz:
    """
    O Dispositivo (Receptor) que realiza as ações.
    """
    def __init__(self, localizacao: str):
        self.localizacao = localizacao

    def ligar(self) -> None:
        print(f"{self.localizacao}: Luz acesa.")

    def desligar(self) -> None:
        print(f"{self.localizacao}: Luz apagada.")

class Termostato:
    """
    Outro Dispositivo (Receptor) para demonstrar a flexibilidade.
    """
    def aumentar_temperatura(self, graus: int) -> None:
        print(f"Termostato: Temperatura aumentada em {graus}°C.")
3. Comandos Concretos
Cada classe de comando concreto encapsula uma única ação, ligando o Invocador ao Receptor específico.

Python

# 3. Comandos Concretos - Encapsulam a requisição
class ComandoLigarLuz(Comando):
    """Comando para ligar uma luz específica."""
    def __init__(self, luz: Luz):
        # Armazena o Receptor (a instância de Luz)
        self._luz = luz 

    def executar(self) -> None:
        self._luz.ligar()

class ComandoAumentarTemperatura(Comando):
    """Comando para aumentar a temperatura de um termostato."""
    def __init__(self, termostato: Termostato, graus: int):
        self._termostato = termostato
        self._graus = graus

    def executar(self) -> None:
        self._termostato.aumentar_temperatura(self._graus)
4. Invocador (Invoker)
O Invocador armazena o comando e o executa. Ele não tem ideia do que o comando fará ou para qual objeto ele está delegando a ação.

Python

# 4. Invocador (Invoker) - Aciona o comando sem conhecer o Receptor
class ControleRemoto:
    """
    O Invocador, que contém o botão e a referência genérica ao Comando.
    """
    def __init__(self):
        self._slot: Comando = None

    def configurar_comando(self, comando: Comando) -> None:
        """Permite parametrizar o slot do controle com qualquer Comando."""
        self._slot = comando

    def pressionar_botao(self) -> None:
        """O Invocador apenas chama 'executar()', sem se importar com os detalhes."""
        if self._slot:
            print("--- Botão Pressionado ---")
            self._slot.executar()
        else:
            print("Nenhum comando configurado para este botão.")
🧪 Código Cliente e Execução
O Cliente é o código que monta e configura as peças (o cérebro da operação).

Python

if __name__ == "__main__":
    # 1. Criação dos Receptores
    luz_sala = Luz("Sala de Estar")
    termostato_central = Termostato()
    
    # 2. Criação do Invocador
    controle = ControleRemoto()

    # 3. Criação e Configuração de Comandos

    # Cenário A: Ligar a Luz
    comando_ligar = ComandoLigarLuz(luz_sala)
    controle.configurar_comando(comando_ligar)
    controle.pressionar_botao()
    
    # Saída:
    # --- Botão Pressionado ---
    # Sala de Estar: Luz acesa.

    print("-" * 30)

    # Cenário B: Aumentar a Temperatura
    comando_aquecer = ComandoAumentarTemperatura(termostato_central, 3)
    controle.configurar_comando(comando_aquecer)
    controle.pressionar_botao()

    # Saída:
    # --- Botão Pressionado ---
    # Termostato: Temperatura aumentada em 3°C.
🚀 Benefícios Demonstrados
O exemplo acima ilustra o principal benefício do Padrão Command:

Desacoplamento: A classe ControleRemoto (Invocador) é totalmente genérica. Ela não contém nenhuma lógica de luz.ligar() ou termostato.aumentar_temperatura(). Ela apenas interage com a interface Comando através do método executar().

Flexibilidade: O comportamento do Invocador é alterado dinamicamente (em runtime) simplesmente configurando um novo objeto Comando no seu slot, sem a necessidade de modificar o código do controle remoto.

Extensibilidade: Para adicionar um novo dispositivo (como um ventilador ou TV), basta criar novas classes ComandoVentiladorLigar e Ventilador (Receptor) sem tocar nas classes ControleRemoto ou Luz.