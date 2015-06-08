#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
using namespace std;


class Solution {

	public:
		vector<int> twoSum(vector<int>& nums, int target) {
			typedef pair<int,int> pii;
			vector<pii> num;
			for (int i = 0; i < nums.size(); ++i)
				num.push_back(make_pair(nums[i], i));
			sort(num.begin(), num.end());
			int i = 0, j = num.size() - 1;
			while (i < j) {
				int tmp = num[i].first + num[j].first;
				if (tmp < target) ++i;
				else if (tmp > target) --j;
				else {
						vector<int> ans(2);
						ans[0] = num[i].second + 1;
						ans[1] = num[j].second + 1;
						if (ans[0] > ans[1])
							swap(ans[0], ans[1]);
						return ans;
				}
			}
		}

};

int main () {
	int numbers[] = {2, 7, 11, 15};
	int target = 9;
	vector<int> nums;
	for (int i = 0; i < 4; ++i)
		nums.push_back(numbers[i]);
	Solution so;
	vector<int> ans = so.twoSum(nums, target);
	printf("%d %d\n", ans[0], ans[1]);

	return 0;
}
