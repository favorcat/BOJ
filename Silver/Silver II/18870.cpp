#include <bits/stdc++.h>
using namespace std;

int n, m, x;
vector <int> v, idx;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

	cin >> n;
	for(int i=0; i<n; i++){
		cin >> x;
		v.push_back(x);
	}

	idx = v;
	sort(idx.begin(), idx.end());
	idx.erase(unique(idx.begin(), idx.end()), idx.end());

	for(int i=0; i<n; i++){
		cout << lower_bound(idx.begin(), idx.end(), v[i]) - idx.begin() << ' ';
	}
}