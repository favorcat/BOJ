#include <bits/stdc++.h>
using namespace std;

int n;
int arr[31];

int main(){
    ios_base::sync_with_stdio(false); 
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n;
    arr[0] = 1;
    arr[1] = 0;
    arr[2] = 3;

    for(int i=4; i<=n; i+=2){
        arr[i] = arr[i-2] * 3;
        for(int j=4; j<=i; j+=2)
            arr[i] += 2 * arr[i-j];
    }
    cout << arr[n];
}