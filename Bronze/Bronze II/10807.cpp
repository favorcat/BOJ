#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false); 
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n, m, v;
    cin >> n;
    int arr[201] = {};

    for(int i=0; i<n; i++){
        cin >> m;
        arr[m+100]++;
    }
    
    cin >> v;
    cout << arr[v+100];
}