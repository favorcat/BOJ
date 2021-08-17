#include <bits/stdc++.h>
using namespace std;

int n, x, y, min_h;
int cnt = 1;
vector< pair<int, int> > meeting;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

	cin >> n;
	for(int i=0; i<n; i++){
		cin >> x >> y;
		meeting.push_back(make_pair(y,x));
	}
	sort(meeting.begin(), meeting.end());

	min_h = meeting[0].first;
	for(int i=1; i<n; i++){
		if (meeting[i].second >= min_h){
			cnt++;
			min_h = meeting[i].first;
		}
	}
	cout << cnt;
}