#include <stdio.h>

struct vendedor{
    char nome[20];
    double fixo, venda, total;
};
int main() {
    struct vendedor funcionario;
    scanf("%[^\n]s",&funcionario.nome);
    scanf("%lf",&funcionario.fixo);
    scanf("%lf",&funcionario.venda);
    funcionario.total = funcionario.fixo + (funcionario.venda*0.15);
    printf("TOTAL = R$ %.2lf\n",funcionario.total);
    return 0;
}