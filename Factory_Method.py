from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        return "Guau"

class Gato(Animal):
    def hablar(self):
        return "Miau"

class AnimalFactory:
    def crear_animal(self, tipo):
        if tipo == "perro":
            return Perro()
        elif tipo == "gato":
            return Gato()
        else:
            raise ValueError("Tipo de animal desconocido")

# Uso
fabrica = AnimalFactory()
animal = fabrica.crear_animal("perro")
print(animal.hablar())
