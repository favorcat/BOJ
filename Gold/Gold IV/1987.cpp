#include <iostream>
#include <algorithm>
using namespace std;

int R, C;
char board[20][20] = {{0,},{0,}};
int visited[26] = {0,};
int ans = 0;

int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

void DFS(int x, int y, int cnt){
    ans = max(ans, cnt);

    for(int i=0; i<4; i++){
        int nextX = x + dx[i];
        int nextY = y + dy[i];

        if(0 <= nextX && nextX < C && 0 <= nextY && nextY < R) {
            int next = board[nextY][nextX] - 65;
            if(visited[next] == 0) {
                visited[next] = 1;
                DFS(nextX, nextY, cnt+1);
                visited[next] = 0;
            }
        }
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> R >> C;
    for(int i=0; i<R; i++){
        for(int j=0; j<C; j++)
            cin >> board[i][j];
    }
    visited[board[0][0]-65] = 1;
    DFS(0,0,1);

    cout << ans;
    return 0;
}