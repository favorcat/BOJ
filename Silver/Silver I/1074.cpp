#include <bits/stdc++.h>
using namespace std;

int n, r, c;
int cnt = 0;

void zFind(int nn, int nr, int nc){
	if (nn == 0) return;
	int m = 1;
	for(int i=1; i<nn; i++) m *= 2;
	// 0
	// 1
	if (nr < m && nc >= m)	cnt += m*m;
	// 2
	if (nr >= m && nc < m)	cnt += m*m*2;
	// 3
	if (nr >= m && nc >= m)	cnt += m*m*3;
	
	if (nr >= m) nr -= m;
	if (nc >= m) nc -= m;
	zFind(nn-1, nr, nc);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

	cin >> n >> r >> c;
	zFind(n, r, c);
	cout << cnt;
}