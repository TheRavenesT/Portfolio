#pragma once
#include <stdlib.h>
#include <stdio.h>

void Somme(int nb1, int nb2) {
	int nb3;
	nb3 = nb1 + nb2;
	printf("Le poids du colis 1 est : %dkg et du colis 2 est : %dkg \n", nb1, nb2);
	printf("La somme des 2 colis est : %dkg \n", nb3);
}

void Randomiser(int* tab){
	for (int i=0; i<(int)sizeof(tab[0]); i++){
		tab[i] = rand() % 40 + 1;
	}
}