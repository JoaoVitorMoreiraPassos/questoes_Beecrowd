#include <stdio.h>
 
int main() {
    int n, maior = 0,posmai,x;
    for(x = 0; x < 100; x++){
        scanf("\%d",&n);
        if(n > maior){
            maior = n;
            posmai = x+1;
        }
    }
    printf("%d\n%d\n",maior,posmai);
 
    return 0;
}