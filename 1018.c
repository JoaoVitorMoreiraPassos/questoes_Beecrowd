#include <stdio.h>
 
int main() {
 
    int valor,n100 = 0,n50 = 0,n20 = 0,n10 = 0,n5 = 0,n2 = 0,n1 = 0;
    scanf("%d",&valor);
    int bckp = valor;
    while(valor >= 100){
        valor -= 100;
        n100 ++;
    }while(valor >= 50){
        valor -= 50;
        n50 ++;
    }while(valor >= 20){
        valor -= 20;
        n20 ++;
    }while(valor >= 10){
        valor -= 10;
        n10 ++;
    }while(valor >= 5){
        valor -= 5;
        n5 ++;
    }while(valor >= 2){
        valor -= 2;
        n2 ++;
    }while(valor >= 1){
        valor -= 1;
        n1 ++;
    }
    printf("%d\n%d nota(s) de R$ 100,00\n%d nota(s) de R$ 50,00\n%d nota(s) de R$ 20,00\n%d nota(s) de R$ 10,00\n%d nota(s) de R$ 5,00\n%d nota(s) de R$ 2,00\n%d nota(s) de R$ 1,00\n",bckp,n100,n50,n20,n10,n5,n2,n1);
    return 0;
}