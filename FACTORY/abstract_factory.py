from abc import ABC, abstractmethod

# =============================
# Abstract Factory
# =============================
class PizzaFactory(ABC):
    @abstractmethod
    def create_pizza_veg(self):
        pass

    @abstractmethod
    def create_pizza_non_veg(self):
        pass

# =============================
# Abstract Products
# =============================

class PizzaVeg(ABC):
    @abstractmethod
    def preparar(self):
        pass

class PizzaNonVeg(ABC):
    @abstractmethod
    def preparar(self):
        pass

    @abstractmethod
    def servir(self):
        pass

# =============================
# Concrete Products - Italianas
# =============================

class PizzaVegItaliana(PizzaVeg):
    def preparar(self):
        print(f'Preparando {type(self).__name__} (Veg Italiana)')


class PizzaNonVegItaliana(PizzaNonVeg):
    def preparar(self):
        print(f'Preparando {type(self).__name__} (Non-Veg Italiana)')

    def servir(self):
        print(f'Servindo {type(self).__name__} com queijo parmesão')

# ================
# =============
# Concrete Products - Brasileiras
# =============================


class PizzaVegBrasileira(PizzaVeg):
    def preparar(self):
        print(f'Preparando {type(self).__name__} (Veg Brasileira)')

class PizzaNonVegBrasileira(PizzaNonVeg):
    def preparar(self):
        print(f'Preparando {type(self).__name__} (Non-Veg Brasileira)')

    def servir(self):
        print(f'Servindo {type(self).__name__} com borda recheada')

# =============================
# Concrete Factories
# =============================

class PizzaItaliana(PizzaFactory):
    def create_pizza_veg(self):
        return PizzaVegItaliana()

    def create_pizza_non_veg(self):
        return PizzaNonVegItaliana()

class PizzaBrasileira(PizzaFactory):
    def create_pizza_veg(self):
        return PizzaVegBrasileira()

    def create_pizza_non_veg(self):
        return PizzaNonVegBrasileira()

# =============================
# Cliente
# =============================

class Pizzaria:
    def fazer_pizzas(self):
        for factory in (PizzaItaliana(), PizzaBrasileira()):
            print(f"\nCriando pizzas da fábrica: {type(factory).__name__}")

            pizza_veg = factory.create_pizza_veg()
            pizza_veg.preparar()

            pizza_non_veg = factory.create_pizza_non_veg()
            pizza_non_veg.preparar()
            pizza_non_veg.servir()

# Execução
if __name__ == "__main__":
    pizzaria = Pizzaria()
    pizzaria.fazer_pizzas()
