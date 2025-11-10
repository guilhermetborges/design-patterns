from abc import ABCMeta, abstractmethod

class ClasseAbstrata(metaclass=ABCMeta):
    def __init__(self):
        pass


    @abstractmethod
    def op1(self):
        pass

    @abstractmethod
    def op2(self):
        pass

    def template_method(self):
        print("algoritmo padrao: op1 após op2")
        self.op2()
        self.op1()



class ClasseConcreta(ClasseAbstrata):
    def op1(self):
        print("op1 feita")

    def op2(self):
        print("op2 feita")



class Client:
    def main(self):
        self.obj = ClasseConcreta()
        self.obj.template_method()



client = Client()
client.main()
