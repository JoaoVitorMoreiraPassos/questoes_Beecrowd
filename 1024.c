#include <stdio.h>
#include <string.h>
int conta_string(char linha[1002]){
	int tam = 0;
	while(linha[tam] != '\0'){
		tam ++;
	}
	return tam;
}
 
int main() {
    int j,numero,c,r;
    char texto[1002];
    scanf("%d",&numero);
    char matriz[numero];
    getchar();
    for(j = 0;j < numero; j ++){
    	int tam;
        gets(texto);
        tam = conta_string(texto);
        char temp[tam];
        for(c = 0; c < tam; c ++){
        	temp[c] = texto[c];
		}
        for(c = 0; c < tam; c++){
            if (temp[c] > 64 && temp[c] < 91 || (temp[c] > 96 && temp[c] < 123)){
                temp[c] = temp[c] + 3;
            }else{
                temp[c] = temp[c];
            }
        }
        r = 0;
        char reversetemp[tam];
        for(c = tam -1; c >=0; c --){
            reversetemp[r] = temp[c];
            r ++;
        }
        for( c = 0; c < tam/2; c ++){
        	temp[c] = reversetemp[c];
		}
		for( c = tam/2; c < tam; c ++){
			temp[c] = reversetemp[c] -1;
		}
		temp[tam]='\0';
		puts(temp);
    }   
    return 0;
}