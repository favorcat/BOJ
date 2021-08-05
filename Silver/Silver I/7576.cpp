#include <bits/stdc++.h>
using namespace std;

int n,m,day = -1;
int tomato[1001][1001];
bool visited[1001][1001];
queue < pair<int, int> > q;

int dx[] = {0, 1, 0, -1};
int dy[] = {1, 0, -1, 0};

void BFS(){
    while (!q.empty()){
        int x = q.front().second;
        int y = q.front().first; 
        q.pop();
        visited[y][x] = true;

        for(int i=0; i<4; i++){
            int nextX = x + dx[i];
            int nextY = y + dy[i];
        
            if (0 <= nextX && nextX < m && 0 <= nextY && nextY < n
                && tomato[nextY][nextX] == 0 && !visited[nextY][nextX]){
                q.push(make_pair(nextY, nextX));
                tomato[nextY][nextX] = tomato[y][x] + 1;
            }
        }
    }
    return;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> m >> n;
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            cin >> tomato[i][j];
            if (tomato[i][j] == 1){
                q.push(make_pair(i, j));
            }
        }
    }
    BFS();
    int flag = 0;
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            if (tomato[i][j] == 0){
                flag = 1;
            }
            day = max(day, tomato[i][j]);
        }
    }
    if (flag == 1) cout << "-1";
    else cout << day-1;
    return 0;
}