#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

#define MAX 200001

using namespace std;

class Edge
{
  public:
    int origin;
    int destination;
    int weight;
};

int is(int vset[], int origin, int destination)
{
    while (vset[origin] > -1)
        origin = vset[origin];
    while (vset[destination] > -1)
        destination = vset[destination];

    if (origin != destination)
    {
        vset[destination] = origin;

        return 1;
    }

    return 0;
}

bool cmp(Edge X, Edge Y)
{
    return X.weight < Y.weight;
}

int main()
{
    int nv = 0;
    int ne = 0;

    int vset[MAX];
    Edge eset[MAX];

    while (cin >> nv >> ne)
    {
        if (nv == 0 && ne == 0)
            break;

        int c = 0;
        int tc = 0;

        memset(vset, -1, sizeof(vset));

        for (int i = 0; i < ne; i++)
        {
            cin >> eset[i].origin >> eset[i].destination >> eset[i].weight;
            tc += eset[i].weight;
        }

        sort(eset, eset + ne, cmp);

        int i = 0;
        int j = 1;

        while (j < nv && i < ne)
        {
            if (is(vset, eset[i].origin, eset[i].destination))
            {
                j++;
                c += eset[i].weight;
            }

            i++;
        }

        cout << tc - c << endl;
    }

    return 0;
}
