#include <bits/stdc++.h>
using namespace std;

int n;
vector <int> dp;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n;
    dp.push_back(1);
    dp.push_back(2);
    for(int i=2; i<n; i++){
        dp.push_back((dp[i-1] + dp[i-2])%10007);
    }
    cout << dp[n-1];
}