#include <iostream>
#include <algorithm>
#include <string>
#include <deque>
using namespace std;

int main(void){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    for(int i=0; i<T; i++){
        int error = 0;
        bool left = true;

        int n;
        string p, num;
        cin >> p >> n >> num;
        int num_len = num.size();
        
        int x = 0;
        deque<int> arr;
        for(int j=0; j<num_len; j++){
            if ('0' <= num[j] && num[j] <= '9') {
                x = x * 10 + (num[j]-48);
            }
            else if (num[j] == ',' || num[j] == ']'){
                arr.push_back(x);
                x = 0;
            }
        }
        
        if (n==0) arr.pop_front();

        int p_len = p.size();
        for(int k=0; k<p_len; k++){
            if (p[k] == 'R')    left = !left; 
            else if (p[k] == 'D'){
                if (arr.empty()) error = 1;
                else {
                    if (left)   arr.pop_front();
                    else        arr.pop_back();
                }
            }
        }

        if (error == 1) cout << "error\n";
        else {
            cout << '[';
            if (left){
                while (!arr.empty()){
                    cout << arr.front();
                    arr.pop_front();
                    if(!arr.empty()) cout << ",";
                }
            }
            else{
                while (!arr.empty()){
                    cout << arr.back();
                    arr.pop_back();
                    if(!arr.empty()) cout << ",";
                }
            }
            cout << "]\n";
        }
    }
    return 0;
}