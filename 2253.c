#include <stdio.h>
#include <string.h>

int main(){
    char senha[48];
    setbuf(stdin,NULL);
    while(scanf(" %[^\n]s",&senha) != EOF){
        int maiscula = 0, minuscula = 0, numero = 0,especial = 0,c;
        for(c = 0; c < strlen(senha); c ++ ){
            if(senha[c] > 64 && senha[c] < 91){
                maiscula ++;
            }else if(senha[c] > 96 && senha[c] < 122){
                minuscula ++;
            }else if(senha[c] > 47 && senha[c] < 58){
                numero ++;
            }else{
                especial ++;
            }
        }
        if(maiscula > 0 && minuscula > 0 && numero > 0 && especial == 0 && strlen(senha)>=6 && strlen(senha) <=32){
            puts("Senha valida.");
        }else{
            puts("Senha invalida.");
        }
    }
    return 0;
}