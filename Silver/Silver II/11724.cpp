#include <bits/stdc++.h>
using namespace std;

int n, m, a, b;
vector <int> graph[1001];
bool visited[1001];

void DFS(int k){
	visited[k] = true;
	for(int i=0; i<graph[k].size(); i++){
		int next = graph[k][i];
		if (!visited[next]) DFS(next);
	}
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

	cin >> n >> m;
	for(int i=0; i<m; i++){
		cin >> a >> b;
		graph[a].push_back(b);
		graph[b].push_back(a);
	}
	
	int cnt = 0;
	for(int i=1; i<=n; i++){
		if(!visited[i]){
			DFS(i);
			cnt++;
		}
	}
	cout << cnt;
}