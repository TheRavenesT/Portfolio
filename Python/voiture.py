class Voiture:

    type = "Car"
    category = "Vehicule"

    """A quoi ça sert ? """

    def __init__(self,marque,modele,taille = 2.0,puissance = 280) :
        self.puissance = puissance
        self.marque = marque
        self.modele = modele
        self.taille = taille

        """taille par défaut de 2.0 (m)"""

    def rouler(self) :
        print(f"{self.marque} {self.modele} est en train de rouler")

    def puissance(self) :
        print(f"Elle fait {self.puissance} chevaux")