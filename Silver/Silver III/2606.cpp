#include <bits/stdc++.h>
using namespace std;

int n, m, a, b;
int cnt = 0;
vector<int> computer[101]; // 인접 리스트
bool visited[101];

void DFS(int x) {
	visited[x] = true;
	for(int i=0; i<computer[x].size(); i++) {
		int k = computer[x][i];
		if (!visited[k]) {
			DFS(k);
			cnt++;
		}
	}
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

	cin >> n >> m;
	for (int i = 0; i < m; i++) {
		cin >> a >> b;
		computer[a].push_back(b);
		computer[b].push_back(a);
	}
	DFS(1);
	cout << cnt;
}