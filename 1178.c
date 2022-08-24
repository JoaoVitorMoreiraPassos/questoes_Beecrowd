#include <stdio.h>
 
int main() {
 
    double n[100],x;
    int c;
    for(c = 0; c < 100; c++){
        if(c == 0){
            scanf("%lf",&x);
        }
        n[c] = x;
        printf("N[%d] = %.4f\n",c,n[c]);
        x = x / 2;
    }
 
    return 0;
}