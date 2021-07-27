#include <iostream>
#include <algorithm>
using namespace std;

int N;
int cnt = 0;
int chess[14] = {0,};

int check_queen(int row){
    for(int i=0; i<row; i++){
        if ((chess[i] == chess[row]) || (row - i == (abs(chess[row] - chess[i]))))
            return 0;
    }
    return 1;
}

void nqueen(int row){
    if (row == N){
        cnt++;
        return;
    }
    else{
        for(int col=0; col<N; col++){
            chess[row] = col;
            if (check_queen(row))
                nqueen(row+1);
        }
    }
}

int main(void){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;
    nqueen(0);
    cout << cnt;
    return 0;
    
}