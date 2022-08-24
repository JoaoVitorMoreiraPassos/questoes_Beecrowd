#include <stdio.h>
struct valores{
    float med[3];
};
int main() {
 
    struct valores val;
    scanf("%f %f %f",&val.med[0],&val.med[1],&val.med[2]);
    printf("TRIANGULO: %.3f\n",val.med[0]*val.med[2]/2);
    printf("CIRCULO: %.3f\n",3.14159*(val.med[2]*val.med[2]));
    printf("TRAPEZIO: %.3f\n",((val.med[0] + val.med[1])/2)*val.med[2]);
    printf("QUADRADO: %.3f\n",val.med[1] * val.med[1]);
    printf("RETANGULO: %.3f\n",val.med[0] * val.med[1]);
 
    return 0;
}