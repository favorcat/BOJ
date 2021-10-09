#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false); 
    cin.tie(nullptr);
    cout.tie(nullptr);

    int month[] = {31,28,31,30,31,30,31,31,30,31,30,31};
    string week[] = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};

    int m, d;
    cin >> m >> d;
    int total = d;

    for(int i=0; i<m-1; i++)
        total += month[i];

    cout << week[total % 7];
}