#include <bits/stdc++.h>
using namespace std;

int T;
int m, n, k, x, y;
int cabbage[51][51];
bool visited[51][51];
queue < pair<int, int> > q;

int dx[] = {0, 1, 0, -1};
int dy[] = {1, 0, -1, 0};

void reset(){
    for(int i=0; i<m; i++){
        for(int j=0; j<n; j++){
            cabbage[i][j] = 0;
            visited[i][j] = false;
        }
    }
}

void BFS(int qx, int qy){
    q.push(make_pair(qx, qy));

    while (!q.empty()){
        int x = q.front().first;
        int y = q.front().second; 
        q.pop();
        visited[x][y] = true;

        for(int i=0; i<4; i++){
            int nextX = x + dx[i];
            int nextY = y + dy[i];
        
            if (0 <= nextX && nextX < m && 0 <= nextY && nextY < n
                && cabbage[nextX][nextY] == 1 && !visited[nextX][nextY]){
                q.push(make_pair(nextX, nextY));
                visited[nextX][nextY] = true;
            }
        }
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> T;
    for(int i=0; i<T; i++){
        int worm = 0;
        cin >> m >> n >> k;
        reset();
        for(int j=0; j<k; j++){
            cin >> x >> y;
            cabbage[x][y] = 1;
        }

        for(int cy=0; cy<n; cy++){
            for(int cx=0; cx<m; cx++){
                if (cabbage[cx][cy] == 1 && !visited[cx][cy]){
                    BFS(cx, cy);
                    worm++;
                }
            }
        }
        cout << worm << "\n";
    }
    return 0;
}