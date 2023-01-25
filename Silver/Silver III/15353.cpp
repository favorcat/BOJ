#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    string a, b;
    string ans = "";
    int tmp = 0;

    cin >> a >> b;
    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());
    while(a.size() < b.size()) a += '0';
    while(b.size() < a.size()) b += '0';
    for(int i=0; i<a.size(); i++){
        int n = (a[i] - '0' + b[i] - '0' + tmp)%10;
        ans += to_string(n);
        tmp = (a[i] - '0' + b[i] - '0' + tmp)/10;
    }
    if (tmp != 0) ans += to_string(tmp);
    reverse(ans.begin(), ans.end());
    cout << ans << endl;
}
