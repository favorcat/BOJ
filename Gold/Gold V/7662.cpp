#include <bits/stdc++.h>
using namespace std;

int t, k, n;
string order;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> t;
    while(t--){
        multimap < int, int > m;
        cin >> k;
        while(k--){
            cin >> order >> n;
            if (order == "I")
                m.insert(make_pair(n, 1));
            else if (order == "D"){
                if (!m.empty()){
                    if (n == 1)
                        m.erase(prev(m.end()));
                    else if (n == -1)
                        m.erase(m.begin());
                }
            }
        }
        if (m.empty())
            cout << "EMPTY\n";
        else
            cout << prev(m.end()) -> first << " " << m.begin() -> first << "\n";
    }
}