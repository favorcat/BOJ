#include <bits/stdc++.h>
using namespace std;

int testcase, n;

int main(){
    ios_base::sync_with_stdio(false); 
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> testcase;
    for(int i=0; i<testcase; i++){
        map <string, int> m;
        int result = 1;

        cin >> n;
        for(int j=0; j<n; j++){
            string name, kind;
            cin >> name >> kind;
            if (m.find(kind) == m.end())    m.insert({kind,1});
            else    m[kind]++;
        }

        for (auto a : m)    result *= (a.second + 1);
        result -= 1;
        cout << result << '\n';
    }
}