nom = "test"
prenom = "re"

print(f"Nom: {nom}\n prénom : {prenom}")
print("hello")

scanf1 = int(input("Rentrer un nombre \n"))
scanf2 = int(input("Renter un 2e nombre \n"))
scanf3 = scanf1 + scanf2

print(f"La somme des 2 valeurs est : {scanf3}")
3
print()

#Exemple : 

class Bird:
    def __init__(self,name,size: 4.5):
        """CONSTRUCTOR"""

        self.name = name
        self.size = size

    def fly(self) :
        print (f"{self.name} is flying")

#Essai :

class Voiture:

    type = "Car"
    category = "Vehicule"

    """A quoi ça sert ? """

    def __init__(self,marque,modele,taille: 2.0) :
        self.marque = marque
        self.modele = modele
        self.taille = taille

        """taille par défaut de 2.0 (m)"""

    def rouler(self) :
        print(f"{self.marque} {self.modele} est en train de rouler")

if __name__ == '__main__' :

    car01 = Voiture("Subaru", "Impreza", 2.3)
    
    print(Voiture.category)