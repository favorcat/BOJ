#include <bits/stdc++.h>
using namespace std;

int T, m;
int arr[50] = {0,1,};

int fibonacci(int n){
    if (n == 0 || n == 1)
        return arr[n];
    else if (arr[n] == 0)
        arr[n] = fibonacci(n-1) + fibonacci(n-2);
    return arr[n];
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> T;
    for (int i=0; i<T; i++){
        cin >> m;
        if (m == 0) cout << "1 0\n";
        else cout << fibonacci(m-1) << " " << fibonacci(m) << "\n";
    }

    return 0;
}