#include <bits/stdc++.h>
using namespace std;

int t, n, m, x, y;

int gcd(int a, int b){
    if(a % b == 0) return b;
    return gcd(b, a % b);
}

int lcm(int a, int b){
    return a * b / gcd(a,b);
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> t;
    for(int i=0; i<t; i++){
        cin >> m >> n >> x >> y;
        int limit = lcm(m, n);
        int j;
        for(j=x; j<=limit; j+=m){
            int num = j % n;
            if (num==0) num = n;
            if (num==y) break;
        }
        if (j > limit) cout << -1 << "\n";
        else cout << j << "\n";
    }
}