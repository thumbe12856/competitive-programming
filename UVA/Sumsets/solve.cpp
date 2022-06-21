#include <iostream>
#include <vector>
#include <math.h>
#include <string>
#include <set>
#include <map>
#include <limits.h>

using namespace std;

int solve(int N, vector<int>& nums) {
    map<int, set<int>> dc;
    map<int, int> dc_max_d;
    for (int i = 0; i < N; i ++) {
        for (int j = i + 1; j < N; j ++) {
            int diff1 = nums[i] - nums[j];
            int diff2 = nums[j] - nums[i];
            dc[diff1].insert(i);
            dc[diff1].insert(j);
            dc_max_d[diff1] = max(dc_max_d[diff1], nums[i]);

            dc[diff1].insert(i);
            dc[diff2].insert(j);
            dc_max_d[diff2] = max(dc_max_d[diff2], nums[j]);
        }
    }

    int ans = INT_MIN;
    for (int i = 0; i < N; i ++) {
        for (int j = i + 1; j < N; j ++) {
            int s = nums[i] + nums[j];
            if (dc.find(s) != dc.end()) {
                if (dc[s].find(i) == dc[s].end() && dc[s].find(j) == dc[s].end()) {
                    ans = max(ans, dc_max_d[s]);
                }
            }
        }
    }
    return ans;
}


int main() {

    int N;
    while (cin >> N) {
        if (N == 0) {
            break;
        }

        vector<int> nums(N);
        for (int i = 0; i < N; i ++) {
            cin >> nums[i];
        }

        int ans = solve(N, nums);
        if (ans == INT_MIN) {
            cout << "no solution" << endl;
        } else {
            cout << ans << endl;
        }
    }

    return 0;
}
