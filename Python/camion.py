class Camion:

    type = "Camion"
    category = "Vehicule"

    def __init__(self,marque,modele,taille: 10) :
        self.marque = marque
        self.modele = modele
        self.taille = taille

    def rouler(self) :
        print(f"{self.marque} {self.modele} est en train de livrer le colis Amazon")