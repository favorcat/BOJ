#include <bits/stdc++.h>
using namespace std;

int n, x;
priority_queue < int > pq;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n;
    for(int i=0; i<n; i++){
        cin >> x;
        if (x==0){
            if(pq.size()){
                cout << pq.top() << "\n";
                pq.pop();
            }
            else cout << "0\n";
        }
        else{
            pq.push(x);
        }
    }
}