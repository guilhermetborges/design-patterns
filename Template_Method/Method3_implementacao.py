from abc import ABCMeta, abstractmethod

class Viagem(metaclass=ABCMeta):

    @abstractmethod
    def ida(self):
        pass

    @abstractmethod
    def dia1(self):
        pass

    @abstractmethod
    def dia2(self):
        pass

    @abstractmethod
    def volta(self):
        pass
    
    @abstractmethod
    def chegada(self):
        pass

    @abstractmethod
    def descanso(self):
        pass



    def itinerario(self):
        self.ida()
        self.dia1()
        self.dia2()
        self.volta()
        self.chegada()
        

class ViagemContada(Viagem):
    def ida(self):
        print("indo para o destino")


    
    def dia1(self):
        print("primeiro dia de viagem foi otimo")

    
    def dia2(self):
        print("primeiro dia de viagem foi ruin")

    
    def volta(self):
        print("voldanto pra casa")

    def chegada(self):
        print("cheguei em casa")


class ViagemMineiros(Viagem):
    def ida(self):
        print("indo para o destino")


    
    def dia1(self):
        print("primeiro dia de viagem foi otimo  fui na fazenda")

    
    def dia2(self):
        print("primeiro dia de viagem foi top fui em tal lugar")

    
    def volta(self):
        print("voltando pra goiania")

    def chegada(self):
        print("cheguei em casa")


class Viajando(ViagemContada):

    def preparar(self):
        opc = int(input("digite a opção de viagem escolhida 1[supresa] 2[mineiros]:\n"))

        if opc == 1:
            self.obj = ViagemContada()
            self.obj.itinerario()
        elif opc == 2:
            self.obj = ViagemMineiros()
            self.obj.itinerario()
        else:
            print('opc invalida')



cliente = Viajando()
cliente.preparar()

