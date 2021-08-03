#include <bits/stdc++.h>
using namespace std;

int n,a,x;
deque<int> order;
deque<int> card;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n;
    for(int i=0; i<n; i++){
        cin >> a;
        order.push_back(a);
    }
    for(int i=1; i<=n; i++){
        x = order.back();
        order.pop_back();
        if (x == 1){
            card.push_front(i);
        }
        else if (x == 2){
            card.insert(card.cbegin()+1, i);
        }
        else if (x == 3){
            card.push_back(i);
        }
    }
    for(int i=0; i<n; i++){
        cout << card[i] << " ";
    }

    return 0;
}