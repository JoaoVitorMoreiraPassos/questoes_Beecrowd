#include <stdio.h>
 
int main(){
    int x,y,cont,c, nn;
    scanf("%d",&c);
    for(x = 0;x < c; x ++){
        cont = 0;
        nn = 0;
        scanf("%d",&nn);
        for (y = 1; y <=nn; y ++){
            if(nn % y == 0){
                cont = cont + 1;
            }
        }if(cont > 2){
            printf("%d nao eh primo\n",nn);
        }else{
            printf("%d eh primo\n",nn);
        }
    }
    return 0;
}