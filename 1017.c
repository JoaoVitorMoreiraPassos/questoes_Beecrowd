#include <stdio.h>
struct viagem{
  int h, v;
  float s;  
};
int main() {
 
    struct viagem var;
    scanf("%d",&var.h);
    scanf("%d",&var.v);
    var.s = var.h * var.v;
    printf("%.3f\n",var.s/12.0);
 
    return 0;
}