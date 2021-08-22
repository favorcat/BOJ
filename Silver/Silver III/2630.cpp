#include <bits/stdc++.h>
using namespace std;

int n;
int paper[128][128];
int white = 0, blue = 0;

void squrefind(int bx, int by, int m){
	int flag = -1;
	for(int j=0; j<m; j++){
		for(int k=0; k<m; k++){
			int x = bx+k, y = by+j;
			if (paper[y][x] == 1){
				if (flag == 0 || flag == 3) flag = 3;
				else flag = 1;
			}
			else if (paper[y][x] == 0){
				if (flag == 1 || flag == 3) flag = 3;
				else flag = 0;
			}
		}
	}
	if (flag == 1) blue++;
	else if (flag == 0) white++;
	else if (flag == 3){
		int num = m/2;
		squrefind(bx, by, num);
		squrefind(bx, by+num, num);
		squrefind(bx+num, by, num);
		squrefind(bx+num, by+num, num);
	}
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

	cin >> n;
	for(int i=0; i<n; i++){
		for(int j=0; j<n; j++){
			cin >> paper[i][j];
		}
	}
	squrefind(0, 0, n);
	cout << white << "\n" << blue;
}