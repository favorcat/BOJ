#include <bits/stdc++.h>
using namespace std;

int n, m;
int arr[8];

void DFS(int x){
    if (x == m){
        for(int i=0; i<m; i++)
            cout << arr[i] << " ";
        cout << "\n";
        return;
    }
    for(int i=1; i<=n; i++){
        arr[x] = i;
        DFS(x+1);
    }
}

int main(){
    ios_base::sync_with_stdio(false); 
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n >> m;
    DFS(0);
}