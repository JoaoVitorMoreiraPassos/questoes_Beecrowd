#include <stdio.h>
 
int main() {
 
    double n1,n2,n3;
    scanf("%lf",&n1);
    scanf("%lf",&n2);
    scanf("%lf",&n3);
    double soma = (n1*2) + (n2* 3) + (n3 * 5);
    double media = soma / 10.0;
    printf("MEDIA = %.1lf\n",media);
 
    return 0;
}