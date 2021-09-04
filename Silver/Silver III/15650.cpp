#include <bits/stdc++.h>
using namespace std;

int n, m;
int arr[9];
bool visited[9];

void DFS(int x, int cnt){
    if (cnt == m){
        for(int i=0; i<m; i++)
            cout << arr[i] << " ";
        cout << "\n";
    }
    for(int i=x; i<=n; i++){
        if(!visited[i]){
            visited[i] = true;
            arr[cnt] = i;
            DFS(i+1, cnt+1);
            visited[i] = false;
        }
    }
}

int main(){
    ios_base::sync_with_stdio(false); 
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n >> m;
    DFS(1,0);
}