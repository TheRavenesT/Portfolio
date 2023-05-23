class Moto:

    type = "Moto"
    category = "Vehicule"

    def __init__(self,marque,modele,taille = 1.0,puissance = 94) :
        self.marque = marque
        self.modele = modele
        self.taille = taille
        self.puissance = puissance

    def rouler(self) :
        print(f"{self.marque} {self.modele} est en train de dévorer l'asphalte")

    def puissance(self) :
        print(f"Elle fait {self.puissance} chevaux")