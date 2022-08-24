#include <stdio.h>

int main(){
    long long int escolhido,loop,cont = 0;
    scanf("%lld",&loop);
    while(1){
        if(cont == loop){
            break;
        }
        scanf("%lld",&escolhido);
        long long int x = 0,xx = 1,y,c;
        for (c = 0 ;c <= escolhido; c ++){
        	if(c <=1){
        		y = c;
			}else{
	    		y = x + xx;
	    		x = xx;
	    		xx = y;
    		}
        }
        printf("Fib(%lld) = %lld\n",escolhido,y);
        cont ++;
    }
    return 0;
}