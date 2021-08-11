#include <bits/stdc++.h>
using namespace std;

#define MAX 100001
int n, k;
int ans = 0;
bool visited[MAX];
queue < pair<int, int> > q;

void BFS(int n, int k){
    q.push(make_pair(n, 0));
    visited[n] = true;

    while (!q.empty()){
        int x = q.front().first;
        int sec = q.front().second;
        q.pop();
        visited[x] = true;

        if (x == k){
            ans = sec;
            break;
        }
        if (x + 1 < MAX && !visited[x + 1]){
            q.push(make_pair(x+1, sec+1));
            visited[x+1] = true;
        }
        if (0 <= x-1 && !visited[x - 1]){
            q.push(make_pair(x-1, sec+1));
            visited[x-1] = true;
        }
        if (x * 2 < MAX && !visited[x * 2]){
            q.push(make_pair(x*2, sec+1));
            visited[x*2] = true;
        }
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n >> k;
    BFS(n, k);
    cout << ans << "\n";
    return 0;
}