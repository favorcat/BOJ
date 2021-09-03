#include <bits/stdc++.h>
using namespace std;

int n, m;
int arr[9];
bool visited[9];

void DFS(int x){
    if (x == m){
        for(int i=0; i<m; i++)
            cout << arr[i] << " ";
        cout << "\n";
    }
    for(int i=1; i<=n; i++){
        if(!visited[i]){
            visited[i] = true;
            arr[x] = i;
            DFS(x+1);
            visited[i] = false;
        }
    }
}

int main(){
    ios_base::sync_with_stdio(false); 
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n >> m;
    DFS(0);
}