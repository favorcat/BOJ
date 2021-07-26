#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main(void){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    string cal;
    int s[21] = {0,};

    cin >> n;

    for(int i = 0; i<n; i++){
        cin >> cal;
        if (cal == "add"){
            cin >> m;
            s[m] = 1;
        }
        else if (cal == "remove"){
            cin >> m;
            s[m] = 0;
        }
        else if (cal == "check"){
            cin >> m;
            if (s[m] == 1)
                cout << "1\n";
            else
                cout << "0\n";
        }
        else if (cal == "toggle"){
            cin >> m;
            if (s[m] == 1)
                s[m] = 0;
            else if (s[m] == 0)
                s[m] = 1;
        }
        else if (cal == "all"){
            for (int k = 0; k<21; k++)
                s[k] = 1;
        }
        else if (cal == "empty"){
            for (int k = 0; k<21; k++)
                s[k] = 0;
        }
    }

}