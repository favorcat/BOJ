#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false); 
    cin.tie(nullptr);
    cout.tie(nullptr);

    int E, S, M;
    cin >> E >> S >> M;

    int year = 1;
    while(true){
        if((year-E) % 15 == 0 &&
            (year-S) % 28 == 0 &&
            (year-M) % 19 == 0) break;
        year++;
    }
    cout << year;
}