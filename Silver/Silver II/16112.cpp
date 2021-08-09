#include <bits/stdc++.h>
using namespace std;

int n, k, x;
long long EXP = 0;
vector <long long> a;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n >> k;
    for(int i=0; i<n; i++){
        cin >> x;
        a.push_back(x);
    }
    sort(a.begin(), a.end());

    for(int i=0; i<=n; i++){
        if (i < k)
            EXP += a[i] * i;
        else
            EXP += a[i] * k;
    }
    cout << EXP;
    return 0;
}