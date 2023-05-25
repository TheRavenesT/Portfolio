#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "Header-EX2.h"

typedef struct Package {
	int Camion;
	int Colis[3];
} CAMIONNEUR ;

struct Random {
	int nombre[10];
};

struct Random test;

CAMIONNEUR package;

enum semaine {
	LUNDI = 1,
	MARDI = 2,
	MERCREDI = 3,
	JEUDI = 4,
	VENDREDI = 5
};


int main(){
	printf("Le jour de livrasion est %d", MARDI);
	srand ( time(NULL)); //Pour Rand les autres fonctions
	Randomiser(package.Colis);
	Somme(package.Colis[0], package.Colis[2]);
	printf("Le nombre de colis est : %d",(int)sizeof(package.Colis[0]));
}

//typedef
//union - Une struct qui ne peut contenir qu'une valeur à la fois
//enumération 



