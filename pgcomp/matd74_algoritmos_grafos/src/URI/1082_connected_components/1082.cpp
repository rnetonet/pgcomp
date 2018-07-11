#include <stdio.h>
#include <vector>
#include <string.h>
#include <algorithm>

using namespace std;

int adj[30][30];
int visitados[30];
vector<int> ordem;
int V, E;

bool handling(int i, int j){ return (i<j); }

void dfs(int p)
{
	visitados[p]=1;
	ordem.push_back(p);
	for(int i=0;i<V;i++)
	{
		if(adj[p][i])
		{
			if(!visitados[i])
			{
				dfs(i);
			}
		}
	}
}

int main(void)
{
	int t;
	scanf("%d", &t);
	for(int k=0;k<t;k++)
	{
		printf("Case #%d:\n", k+1);
		scanf("%d %d", &V, &E);
		char foo, bar;
		int cont = 0;
		ordem.clear();
		memset(adj,0,sizeof(adj));
		memset(visitados,0,sizeof(visitados));
		for(int i=0;i<E;i++)
		{
			scanf("\n%c %c", &foo, &bar);
			adj[(int)foo-97][(int)bar-97]=adj[(int)bar-97][(int)foo-97]=1;
		}
	
		for(int i=0;i<V;i++)
		{
			if(!visitados[i])
			{
				cont++;
				dfs(i);
				sort(ordem.begin(),ordem.end(),handling);
				for(int j=0;j<(ordem.size());j++)
				{
                    printf("\n *** %d\n", ordem[j]);
					printf("%c,",ordem[j]+97);
				}
				printf("\n");
			}
			ordem.clear();
		}

		printf("%d connected components\n",cont);
		printf("\n");
	}
	return 0;	
}