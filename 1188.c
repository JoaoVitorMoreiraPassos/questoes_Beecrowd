#include <stdio.h>
 
int main() {
 
    char o;
    int i,j,x = 10,y = 1,cont = 0;
    double matriz[12][12],soma = 0,media;
  	scanf("%c",&o);
    for(i = 0;i < 12; i ++){
        for(j = 0;j < 12; j ++){
            scanf("%lf",&matriz[i][j]);
        };
    }
    if(o =='S'){
	    for(i = 11; i > 6; i --){
	        for(j = x; j > 0; j--){
	            soma = soma + matriz[i][j];
	            if(j == y){
	            	j = 0;
				}
	    	}
	    	y ++;
	    	x --;
	    }
	    printf("%.1f\n",soma);
	}else if(o == 'M'){
		for(i = 11; i > 6; i --){
	        for(j = x; j > 0; j--){
	            soma = soma + matriz[i][j];
	            cont ++;
	            if(j == y){
	            	j = 0;
				}
	    	}
	    	y ++;
	    	x --;
		}
		media = soma / cont;
		printf("%.1f\n",media);
	}
    return 0;
}