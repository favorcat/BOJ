#include <bits/stdc++.h>
using namespace std;

int testcase, n;

int main(){
    ios_base::sync_with_stdio(false); 
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> testcase;
    while(testcase--){
        cin >> n;
        long long p[101] = {0, 1, 1};
        for(int i=3; i<=n; i++)
            p[i] = p[i-2] + p[i-3];
        cout << p[n] << '\n';
    }
}