#include <stdio.h>

int main(){
    int n, cont = 1, x;
    scanf("%d",&n);
    for (x = 0; x < n; x ++){
        printf("%d %d %d\n",cont,cont*cont,cont*cont*cont);
        cont ++;
    }
    return 0;
}