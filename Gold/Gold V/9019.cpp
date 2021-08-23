#include <bits/stdc++.h>
using namespace std;

int T, a, b;
string order;
bool visited[100001];

void BFS(){
	queue <pair <int, string> > q;
	q.push(make_pair(a, ""));
	visited[a] = true;

	while (!q.empty()){
		int n = q.front().first;
		order = q.front().second;
		q.pop();
		if (n == b) return;

		// D
		int m = (2 * n) % 10000;
		if(!visited[m]){
			visited[m] = true;
			q.push(make_pair(m, order+"D"));
		}

		// S
		if (n==0) m = 9999; else m = n-1;
		if(!visited[m]){
			visited[m] = true;
			q.push(make_pair(m, order+"S"));
		}

		// L
		m = (n % 1000) * 10 + n / 1000;
		if(!visited[m]){
			visited[m] = true;
			q.push(make_pair(m, order+"L"));
		}
		
		// R
		m = (n / 10) + (n % 10) * 1000;
		if(!visited[m]){
			visited[m] = true;
			q.push(make_pair(m, order+"R"));
		}
	}
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

	cin >> T;
	for(int i=0; i<T; i++){
		memset(visited, false, 100001);
		cin >> a >> b;
		BFS();
		cout << order << "\n";
	}
}