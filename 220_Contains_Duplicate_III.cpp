#include <iostream>
#include <algorithm>
#include <set>
#include <cstdio>
#include <vector>
using namespace std;
#define pb push_back

class Solution {
public:
	bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
		if (k == 0 || t < 0) return false;
		typedef pair<int,int>PII;
		vector<PII>vt;
		for (int i = 0; i < nums.size(); ++i) {
			vt.push_back(make_pair(nums[i], i));	
		}
		sort(vt.begin(), vt.end());
		set<int>ss;
		set<int>::iterator it;
		int i = 0, j = 0;
		while (j < vt.size()) {
			int sum =  vt[j].first - vt[i].first;
			while (i < j && (sum > t || (vt[j].first > vt[i].first && sum < 0))) {
				ss.erase(vt[i].second);
				++i;
				if (i < j) sum =  vt[j].first - vt[i].first;
			}
			if (ss.size() >= 1) {
				it = ss.lower_bound(vt[j].second - k);
				if (it != ss.end() && *it <= vt[j].second + k) {
					return true;	
				}
			}
			ss.insert(vt[j].second);
			++j;
		}
		return false;
	}
};

int main () {
	Solution so;
	vector<int>vt;
	//vt.pb(1); vt.pb(9); vt.pb(20); vt.pb(4);
	//vt.pb(1); vt.pb(3); vt.pb(1);
	vt.pb(3); vt.pb(6); vt.pb(0); vt.pb(4);
	//vt.pb(-3); vt.pb(3);
	printf("%d\n", so.containsNearbyAlmostDuplicate(vt, 2, 2));
	return 0;
}
