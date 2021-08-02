#include <bits/stdc++.h>
using namespace std;

int n, k, d, ans;
int arr[1001] = {0};
int cnt = 0;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n >> k;
    for(int i=2; i<=n; i++){
        arr[i] = 1;
    }
    for(int i=2; i<=n; i++){
        if (arr[i] == 1){
            for(int j=i; j<=n; j+=i){
                if (arr[j] == 1) {
                    arr[j] = 0;
                    cnt++;
                    if (cnt == k) {
                        cout << j;
                        break;
                    }
                }
            }
        }
    }
    return 0;
}