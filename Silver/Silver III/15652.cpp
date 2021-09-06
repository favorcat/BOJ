#include <bits/stdc++.h>
using namespace std;

int n, m;
int arr[9];

void DFS(int x, int cnt){
    if (cnt == m){
        for(int i=0; i<m; i++)
            cout << arr[i] << " ";
        cout << "\n";
        return;
    }
    for(int i=x; i<=n; i++){
        arr[cnt] = i;
        DFS(i, cnt+1);
    }
}

int main(){
    ios_base::sync_with_stdio(false); 
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n >> m;
    DFS(1,0);
}