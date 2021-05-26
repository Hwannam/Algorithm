#include <iostream>
#include <queue>
using namespace std;

struct status{
	int rot_num, rx,ry,bx,by;
};

int N, M;
char map[10][10];
bool check[10][10][10][10];
queue<status> q;
const int dx[] = { -1, 0, 1, 0 }, dy[] = { 0, 1, 0, -1 };

void move(int& x, int& y, int& c, int dx, int dy) {
    while (map[x + dx][y + dy] != '#' && map[x][y] != 'O') {
        x += dx;
        y += dy;
        c += 1;
    }
}

void bfs() {
    while (!q.empty()) {
        int rx = q.front().rx, ry = q.front().ry;
        int bx = q.front().bx, by = q.front().by;
        int rot_num = q.front().rot_num; 
        q.pop();
        if (rot_num >= 10) break;

        for (int i = 0; i < 4; i++) {
            int nrx = rx, nry = ry, nbx = bx, nby = by;
          
            int rc = 0, bc = 0;
            int nrot = rot_num + 1;
            move(nrx, nry, rc, dx[i], dy[i]); 
            move(nbx, nby, bc, dx[i], dy[i]); 
            if (map[nbx][nby] == 'O') continue; 
            if (map[nrx][nry] == 'O') {   
                cout << nrot << "\n";
                return;
            }
            if (nrx == nbx && nry == nby) {
                if (rc > bc) nrx -= dx[i], nry -= dy[i]; 
                else nbx -= dx[i], nby -= dy[i];
            }
            if (check[nrx][nry][nbx][nby]) continue; 
            check[nrx][nry][nbx][nby] = true;
            q.push({  nrot,nrx, nry, nbx, nby});
        }
    }
    cout << -1 << "\n";
}


int main()
{
    cin >> N >> M;
    int rx = 0, ry = 0, bx = 0, by = 0;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> map[i][j];
            if (map[i][j] == 'R') rx = i, ry = j;
            else if (map[i][j] == 'B') bx = i, by = j;
        }
    }
    q.push({0, rx, ry, bx, by });
    check[rx][ry][bx][by] = true;
    bfs();

	return 0;
}
