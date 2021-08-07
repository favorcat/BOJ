#include <bits/stdc++.h>
using namespace std;

int N,M,H,day = -1;
int tomato[101][101][101];
bool visited[101][101][101];
struct box{
    int boxH;
    int boxN;
    int boxM;
};
queue <box> q;

int dx[] = {1,-1,0,0,0,0};
int dy[] = {0,0,1,-1,0,0};
int dz[] = {0,0,0,0,1,-1};

void BFS(){
    while (!q.empty()){
        int x = q.front().boxM;
        int y = q.front().boxN;
        int z = q.front().boxH;
        q.pop();
        visited[z][y][x] = true;

        for(int i=0; i<6; i++){
            int nextX = x + dx[i];
            int nextY = y + dy[i];
            int nextZ = z + dz[i];
        
            if (0 <= nextX && nextX < M && 0 <= nextY && nextY < N && 0 <= nextZ && nextZ < H
                && tomato[nextZ][nextY][nextX] == 0 && !visited[nextZ][nextY][nextX]){
                q.push({nextZ, nextY, nextX});
                tomato[nextZ][nextY][nextX] = tomato[z][y][x] + 1;
            }
        }
    }
    return;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> M >> N >> H;
    for(int i=0; i<H; i++){
        for(int j=0; j<N; j++){
            for(int k=0; k<M; k++){
                cin >> tomato[i][j][k];
                if (tomato[i][j][k] == 1){
                    q.push({i, j, k});
                }
            }
        }
    }

    BFS();
    int flag = 0;
    for(int i=0; i<H; i++){
        for(int j=0; j<N; j++){
            for(int k=0; k<M; k++){
                if (tomato[i][j][k] == 0){
                    flag = 1;
                }
                day = max(day, tomato[i][j][k]);
            }
        }
    }
    if (flag == 1) cout << "-1";
    else cout << day-1;
    return 0;
}