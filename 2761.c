#include <stdio.h>

int main(){
    int n;
    float num;
    char caractere;
    char frase[50];
    
    scanf("%d %f %c %[^\n]s",&n,&num,&caractere,&frase);
    printf("%d%f%c%s\n", n, num, caractere, frase);
    printf("%d\t%f\t%c\t%s\n",n, num, caractere, frase);
    printf("%10d%10f%10c%10s\n",n, num, caractere, frase);
    
    return 0;
}