#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "Header-EX2.h"

struct Package {
	int Camion;
	int Colis[3];
};

struct Random {
	int nombre[10];
};

struct Random test;

struct Package package;

int main(){
	srand ( time(NULL));
	Randomiser(package.Colis);
	Somme(package.Colis[0], package.Colis[2]);
	printf("Le nombre de colis est : %d",(int)sizeof(package.Colis[0]));
}

//typedef
//union 
//enumération



