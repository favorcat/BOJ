#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false); 
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n, tmp = 0;
    cin >> n;
    int p[n];
    vector<int> v;

    for(int i=0; i<n; i++) {
        cin >> p[i];
        if (i>0 && p[i-1] < p[i]) tmp += p[i]-p[i-1];
        else if (p[i-1] >= p[i]) {
            v.push_back(tmp); tmp = 0;
        }
    }
    if (tmp != 0) v.push_back(tmp);
    cout << *max_element(v.begin(), v.end());
}