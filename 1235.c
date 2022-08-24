#include <stdio.h>
#include <string.h>

int conta_string(char linha[102]){
	int tam = 0;
	while(linha[tam] != '\0'){
		tam ++;
	}
	return tam;
}

int main(){
	
	int n,i;
	scanf("%d",&n);
	getchar();
	for(i = 0; i < n; i ++){
		char linha[102];
		gets(linha);
		int tam,c;
		tam = conta_string(linha);
		char linha_invertida[tam];
		int cont = 0;
		for(c = (tam/2)-1; c >=0; c --){
			linha_invertida[cont] = linha[c];
			cont ++;
		}
		for(c = tam -1; c > (tam/2)-1;c --){
			linha_invertida[cont] = linha[c];
			cont ++;
		}	
		linha_invertida[tam] = '\0';

		puts(linha_invertida);
	}		
	return 0;
}