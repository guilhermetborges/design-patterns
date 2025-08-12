# 🏭 Padrão de Projeto: Factory Method

## 🔍 O que é?
O **Factory Method** é um padrão de criação que fornece uma interface para criar objetos em uma superclasse, mas permite que as subclasses alterem o tipo de objetos que serão criados.

Ele ajuda a **desacoplar** a criação do objeto da sua utilização, facilitando a **extensão do sistema** sem modificar o código existente.

---

## 🎯 Intenção
> "Definir uma interface para criar um objeto, mas deixar as subclasses decidirem qual classe instanciar."

---

## 🧱 Estrutura


---

## ✅ Vantagens
- Desacopla o código cliente da criação dos objetos.
- Facilita a manutenção e a adição de novos produtos.
- Segue o **Princípio Aberto/Fechado** (Open/Closed Principle).

---

## ❌ Desvantagens
- Pode aumentar o número de classes no projeto.
- Pode ser mais complexo do que usar `new` diretamente em projetos pequenos.

---

## 💡 Quando usar?
- Quando não se sabe com antecedência qual classe de objetos precisa ser instanciada.
- Quando o código deve trabalhar com interfaces ou classes abstratas.
- Para permitir que subclasses decidam quais objetos criar.

---

## 🧪 Exemplo em Python

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        return "Au Au!"

class Gato(Animal):
    def falar(self):
        return "Miau!"

class AnimalFactory:
    def criar_animal(self, tipo):
        if tipo == "cachorro":
            return Cachorro()
        elif tipo == "gato":
            return Gato()
        else:
            raise ValueError("Tipo de animal desconhecido")

# Cliente
factory = AnimalFactory()
animal = factory.criar_animal("cachorro")
print(animal.falar())  # Saída: Au Au!


| Característica     | Factory Method       | Abstract Factory                               |
| ------------------ | -------------------- | ---------------------------------------------- |
| Criação de objetos | 1 produto por método | Vários produtos relacionados                   |
| Padrão de projeto  | Criacional           | Criacional                                     |
| Estrutura          | Mais simples         | Mais complexa (múltiplos factories e produtos) |
| Herança usada?     | Sim                  | Sim                                            |
