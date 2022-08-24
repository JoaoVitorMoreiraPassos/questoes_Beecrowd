#include <stdio.h>
 
int main() {
    int i;
    float m,cont,soma;
    cont = 0;
    soma = 0;
    do{
        scanf("%d",&i);
        if(i > 0){
        	soma = soma + i;
        	cont = cont + 1;
    	}
    }while (i > 0);
    m = soma / cont;
    printf("%.2f\n",m);
    return 0;
}