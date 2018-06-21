#include <stdio.h>

#define maxN 1000 //quantidade de livros na estante
#define maxC 100  //capacidade da bolsa

int tabela[maxN + 1][maxC + 1];
int peso[maxN + 1];
int interesse[maxN + 1];

int max(int a, int b) {
    if (a >= b)
    {
        return a;
    } else {
        return b;
    }
}

int main()
{

    int capacidade, v, p, i, j, numero, s, soma, contador;
    
    contador = 1;
    
    while (1) //repete o loop até finalizar o número de itens na estante
    {
        scanf("%d %d", &numero, &capacidade); //numero de livros na estante, capacidade da bolsa

        if (numero == 0 && capacidade == 0)
        {
            break;
        }
        
        // lendo o peso de cada livro e o grau de interesse
        for (i = 1; i <= numero; i++)
        {
            scanf("%d %d", &p, &v);
            peso[i] = p;
            interesse[i] = v;
        }

        // zerando a primeira coluna
        for (i = 0; i <= numero; i++)
        {
            for (j = 0; j <= capacidade; j++) 
            {
                tabela[i][j] = 0;
            }
        }

        // iniciando o algoritmo da mochila
        for (i = 1; i <= numero; i++)
        {
            for (j = 1; j <= capacidade; j++)
            {
                if (peso[i] <= j)
                {
                    tabela[i][j] = max(tabela[i - 1][j], interesse[i] + tabela[i - 1][j - peso[i]]);
                } else {
                    tabela[i][j] = tabela[i - 1][j];
                }
            }
        }

        //imprimindo o resultado
        printf("Caso %d: %d\n", contador, tabela[numero][capacidade]);
        contador++;
    }
    return 0;
}
