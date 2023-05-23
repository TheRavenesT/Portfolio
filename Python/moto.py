class Moto:

    type = "Moto"
    category = "Vehicule"

    def __init__(self,marque,modele,taille: 1.0) :
        self.marque = marque
        self.modele = modele
        self.taille = taille

        """taille par défaut de 2.0 (m)"""

    def rouler(self) :
        print(f"{self.marque} {self.modele} est en train de dévorer l'asphalte")