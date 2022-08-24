#include <stdio.h>
struct pecas{
    float val[2][3];
};
int main() {
 
    struct pecas p;
    scanf("%f %f %f",&p.val[0][0],&p.val[0][1],&p.val[0][2]);
    scanf("%f %f %f",&p.val[1][0],&p.val[1][1],&p.val[1][2]);
    float preco = p.val[0][1]*p.val[0][2] + p.val[1][1]*p.val[1][2];
    printf("VALOR A PAGAR: R$ %.2f\n",preco);
    return 0;
}