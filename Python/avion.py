from abc import ABC, abstractmethod

class Avion(ABC):
    @abstractmethod
    def pays(self):
        pass

class Airbus(Avion):

    def pays(self): 
        print("France")

class Boeing(Avion):
    def pays(self):
        print("USA")