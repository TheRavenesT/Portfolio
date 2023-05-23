class Camion:

    type = "Camion"
    category = "Vehicule"

    def __init__(self,marque,modele,taille = 10,poids = 10000) :
        self.poids = poids
        self.marque = marque
        self.modele = modele
        self.taille = taille

    def rouler(self) :
        print(f"{self.marque} {self.modele} est en train de livrer le colis Amazon")

def ShowPoids():
    var = input("Rentrer le poids de la marchandise \n")
    print("Le poids est de :" + var)

ShowPoids() 