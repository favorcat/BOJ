#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

string s;
int a = 0;
int b;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> s;
    int s_len = s.size();
    for (int i=0; i<3; i++){
        string x = "";
        int cnt = -1;
        if (i < s_len){
            a = a * 10 + s[i]-48;
            for (int j=0; j<s_len; j++){
                if (x.size() < s_len){
                    x += to_string(a+j);
                    cnt++;
                }
            }
            if (x == s){
                b = a + cnt;
                cout << a << " " << b;
                break;
            }
        }
    }    
    return 0;
}