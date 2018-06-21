#include <bits/stdc++.h>
#define MAX 100000 + 10
using namespace std;

int main(){

    int t;

    scanf("%d", &t);

    int n,k;

    while(t--){
        scanf("%d %d", &n, &k);

        int d[MAX];
        int pesos[MAX];
        int dp[MAX];

        memset(pesos,0,sizeof pesos);
        memset(dp, 0, sizeof dp);

        for ( int i = 0; i < n; i++ ){
            scanf("%d", &d[i]);
        }

        int aux;

        for ( int i = 0; i < n; i++ ){
            scanf("%d", &aux);
            pesos[d[i]] = max(pesos[d[i]], aux);
        }

        int max_current = pesos[0];

        for ( int i = 0; i < d[n-1] + 1; i++ ){
            if ( i - k >= 0 ){

                max_current = max(max_current, pesos[i] + dp[i-k]);
            }else{

                max_current = max(max_current, pesos[i]);
            }

            dp[i] = max_current;
        }

        printf("%d\n", max_current);
    }

    return 0;
}