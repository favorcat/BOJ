#include <bits/stdc++.h>
using namespace std;

int n, m;
int cnt = 0;
int a[10001];
int L = 0;
int R = 0;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n >> m;
    for(int i=0; i<n; i++){
        cin >> a[i];
    }

    int sum = a[0];

    while(L <= R && R < n){
        if(sum < m)
            sum += a[++R];
        else if (sum == m){
            sum += a[++R];
            cnt++;
        }
        else if (sum > m){
            sum -= a[L++];
            if (L > R && L < n){
                R = L;
                sum = a[L];
            }
        }
    }
    cout << cnt;
    return 0;
}