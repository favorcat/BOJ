#include <bits/stdc++.h>
using namespace std;

#define MAX 1001
int n, m, v;
int graph[MAX][MAX];
bool visited[MAX];
queue<int> q;

void reset(){
    for(int i=1; i<=n; i++) visited[i] = false;
}

void DFS(int v){
    visited[v] = true;
    cout << v << " ";
    for(int i=1; i<=n; i++){
        if(graph[v][i] == 1 && !visited[i]) DFS(i);
    }
}

void BFS(int v){
    q.push(v);
    visited[v] = true;
    cout << v << " ";

    while(!q.empty()){
        v = q.front();
        q.pop();

        for(int i=1; i<=n; i++){
            if(graph[v][i] == 1 && !visited[i]){
                q.push(i);
                visited[i] = true;
                cout << i << " ";
            }
        }
    }
}
int main(){
    ios_base::sync_with_stdio(false); 
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n >> m >> v;
    for(int i=0; i<m; i++){
        int a, b;
        cin >> a >> b;
        graph[a][b] = 1;
        graph[b][a] = 1;
    }

    reset();
    DFS(v);
    cout << '\n';

    reset();
    BFS(v);
}