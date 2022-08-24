#include <stdio.h>
struct carro{
    int km;
    float kml;
};
float calc_consumo(float kml, int km){
    float consumo = km / kml;
    return consumo;
}
int main() {
    
    struct carro consumo;
    scanf("%d",&consumo.km);
    scanf("%f",&consumo.kml);
    printf("%.3f km/l\n",calc_consumo(consumo.kml,consumo.km));
 
    return 0;
}
