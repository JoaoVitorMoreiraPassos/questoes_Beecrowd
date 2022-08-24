#include <stdio.h>

int main(){
    int x,y,a = 1,c;
    scanf("%d %d",&x,&y);
    for(c = 0; c < y; c ++){
        if (a % x != 0){
            printf("%d ",a);
        }else{
            printf("%d\n",a);
        }
        a ++;
    }
}