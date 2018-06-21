#include <bits/stdc++.h>
#define fast ios_base::sync_with_stdio(false);cin.tie(NULL)

using namespace std;

int table[5][5];
int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0, 1, -1};

struct state {
  int x, y;
  state() {}
  state(int x, int y) : x(x), y(y) {}
};

bool bfs(int x, int y) {
  bool vi[5][5];
  memset(vi, false, sizeof(vi));
  queue<state> q;
  vi[x][y] = true;
  q.push(state(x, y));

  while (!q.empty()) {
    state curr = q.front(); q.pop();
    if (curr.x == 4 and curr.y == 4) return true;

    for (int i = 0; i < 4; i++) {
      int nx = dx[i] + curr.x;
      int ny = dy[i] + curr.y;

      if (nx >= 0 and nx < 5 and ny >= 0 and ny < 5 and !vi[nx][ny] and !table[nx][ny]) {
        vi[nx][ny] = true;
        q.push(state(nx, ny));
      }
    }
  }
  return false;
}

int main() {
  fast;
  int t;
  cin >> t;

  while (t--) {
    for (int i = 0; i < 5; i++) {
      for (int j = 0; j < 5; j++) {
        cin >> table[i][j];
      }
    }
    cout << ((bfs(0, 0))? "COPS" : "ROBBERS") << endl;
  }

  return 0;
}