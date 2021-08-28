#include <bits/stdc++.h>
using namespace std;

int h, m;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> h >> m;
    int n = h % 30;
    if (n * 12 == m) cout << 'O';
    else cout << 'X';
}