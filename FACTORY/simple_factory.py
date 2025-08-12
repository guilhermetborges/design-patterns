from abc import ABCMeta, abstractmethod, ABC


class Animal(metaclass=ABCMeta):

    @abstractmethod
    def falar(self):
        pass


class Cachorro(Animal):

    def falar(self):
        print('au au au')


class Gato(Animal):

    def falar(self):
        print('miau miau miau')


class Factory:

    def criar_animal(self,tipo):
        return eval(tipo)().falar()
  
    

if __name__ == "__main__":
    f = Factory()
    animal = input('Qual animal voce deseja?\n')
    obj = f.criar_animal(animal)
