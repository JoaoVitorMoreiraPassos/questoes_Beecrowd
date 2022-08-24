#include <stdio.h>
struct idade{
    int d,m,a;
};
int main() {
 
    struct idade dt;
    dt.a = 0;
    dt.m = 0;
    dt.d = 0;
    int idade;
    scanf("%d",&idade);
    int c;
    while(idade >= 365){
        idade -= 365;
        dt.a ++;
    }
    while(idade >= 30){
        idade -= 30;
        dt.m ++;
    }
    while(idade >= 1){
        idade -= 1;
        dt.d ++;
    }
    printf("%d ano(s)\n%d mes(es)\n%d dia(s)\n",dt.a,dt.m,dt.d);
 
    return 0;
}