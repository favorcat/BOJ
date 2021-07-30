#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main(void){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    string num;
    cin >> num;
    int x = 0;
    int result = 0;
    bool minus = false;
    for(int i=0; i<=num.size(); i++){
        if (num[i] == '-' || num[i] == '+' || num[i] == '\0') {
            if (minus)  result -= x;
            else result += x;
            if (num[i] == '-') minus = true;
            x = 0;
        }
        else if ('0' <= num[i] && num[i] <= '9'){
            x = x * 10 + (num[i]-48);
        }
    }
    cout << result;
    return 0;
}