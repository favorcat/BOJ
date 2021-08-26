#include <bits/stdc++.h>
using namespace std;

int n, m;
int arr[100001];

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n >> m;
    for(int i=1; i<=n; i++){
        int x;
        cin >> x;
        arr[i] = arr[i-1] + x;
    }

    for(int i=0; i<m; i++){
        int a, b;
        cin >> a >> b;
        cout << arr[b] - arr[a-1] << "\n";
    }
}