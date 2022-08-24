#include <stdio.h>
#include <string.h>

int main( void ){
    int i,j,loop,n,cont = 0;;
    
    scanf("%d",&loop);
    for (i = 0; i < loop; i ++)
    {
        cont = 0;
        scanf("%d",&n);
        char idiomas[n][21];
        for (j = 0; j < n; j ++ )
        {
            scanf("%s",&idiomas[j]);
        }
        for (j = 1; j < n; j ++ )
        {
            if(strcmp(idiomas[j],idiomas[j-1]) != 0)
            {
                cont = 1;
                break;
            }
        }
        if(cont == 0)
        {
            printf("%s\n",idiomas[0]);
        }
        else
        {
            printf("ingles\n");
        }
    }
}