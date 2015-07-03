#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;
#define pb push_back

class Solution {
public:
	typedef pair<int,int> pii;
	int maxArea(vector<int>& height) {
		vector<pii> vt;
		for (int i = 0; i < height.size(); ++i)
			vt.push_back(make_pair(height[i], i));
		sort(vt.begin(), vt.end(), greater<pii>());
		return solve(vt);
	}

	int solve(vector<pii>&vt) {
		int res = 0;
		int maxRight = -1;
		for (int i = 0; i < vt.size(); ++i) {
			if (maxRight > vt[i].second) {
				res = max(res, vt[i].first * (maxRight - vt[i].second));
			}
			maxRight = max(maxRight, vt[i].second);
		}
		int maxLeft = vt.size();
		for (int i = 0; i < vt.size(); ++i) {
			if (maxLeft < vt[i].second) {
				res = max(res, vt[i].first * (vt[i].second - maxLeft));
			}
			maxLeft  = min(maxLeft, vt[i].second);
		}
		return res;
	}
};

int main () {

	Solution a;
	vector<int>vt;
	//vt.pb(3); vt.pb(2); vt.pb(5); vt.pb(7); vt.pb(1);
	vt.pb(1);
	vt.pb(1);
	printf("%d\n", a.maxArea(vt));
	return 0;
}
