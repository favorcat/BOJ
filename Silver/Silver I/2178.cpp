#include <bits/stdc++.h>
using namespace std;

int n,m;
int maze[100][100] = {0};
queue < pair<int, int> > q;

int dx[] = {0, 1, 0,- 1};
int dy[] = {-1, 0, 1, 0};

void find(){

    q.push(make_pair(0,0));
    pair <int, int> current;

    while (!q.empty()){

        current = q.front();
        q.pop();

        for(int i=0; i<4; i++){
            int nextX = current.second + dx[i];
            int nextY = current.first + dy[i];
        
            if (0 <= nextX && nextX < m && 0 <= nextY && nextY < n && maze[nextY][nextX] == 1){
                q.push(make_pair(nextY, nextX));
                maze[nextY][nextX] = maze[current.first][current.second] + 1;
            }
        }
    }
    return;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n >> m;
    string s;
    for(int i=0; i<n; i++){
        cin >> s;
        for(int j=0; j<m; j++)
            maze[i][j] = s[j] - '0';
    }
    find();
    cout << maze[n-1][m-1];

    return 0;
}