#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

#define MAX 1001
string a,b;
int LCS[MAX][MAX];

int main(void){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> a >> b;

    int a_len = a.size();
    int b_len = b.size();

    for(int i=1; i<=a_len; i++){
        for(int j=1; j<=b_len; j++){
            if (a[i-1] == b[j-1])
                LCS[i][j] = LCS[i-1][j-1] + 1;
            else
                LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1]);
        }
    }
    cout << LCS[a_len][b_len];
    return 0;
}