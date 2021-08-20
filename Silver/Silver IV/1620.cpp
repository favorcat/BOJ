#include <bits/stdc++.h>
using namespace std;

int n, m, idx;
string name, order;
vector <string> v;
map <string, int> ms;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

	cin >> n >> m;
	for(int i=0; i<n; i++){
		cin >> name;
		v.push_back(name);
		ms.insert(make_pair(name, i+1));
	}
	for(int i=0; i<m; i++){
		cin >> order;
		if('0' <= order[0] && order[0] <= '9'){
			idx = stoi(order);
			cout << v[idx-1] << '\n';
		}
		else{
			cout << ms[order] << '\n';
		}
	}
}