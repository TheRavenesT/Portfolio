import avion
import camion
import moto
import voiture

MyCar = voiture.Voiture("Subaru","Impreza",2.5)
MyBike = moto.Moto("Suzuki","GSR",1.20)

if __name__ == "__main__":

    voiture.Voiture.rouler(MyCar)
    moto.Moto.rouler(MyBike)
    moto.Moto.puissance(MyBike)
    avion.Airbus.pays(avion)