#include <iostream>
#include <algorithm>
using namespace std;

int n;
int arr[1000];

int main(void){
    cin >> n;
    for(int i = 0; i<n; i++){
        cin >> arr[i];
    }
    sort(arr, arr+n);

    int sum = 0;
    for(int i = 0; i<n; i++){
        sum += arr[i]*(n-i);
    }

    cout << sum << endl;
    return 0;
}