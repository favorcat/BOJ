#include <bits/stdc++.h>
using namespace std;

long long n, p, q;
map <long long, long> a;

long long dp(long long x){
    if (a[x]) return a[x];
    else    return a[x] = dp(x/p) + dp(x/q);
}

int main(){
    ios_base::sync_with_stdio(false); 
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n >> p >> q;
    a[0] = 1;
    dp(n);
    cout << a[n];
}