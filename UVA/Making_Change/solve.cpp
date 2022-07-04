#include <vector>
#include <iostream>
#include <climits>
#include <math.h>
#include <string>
#include <vector>
#include <set>

using namespace std;

vector<int> nums(6);
vector<int> value(6);
int s;
int target;
float temp_target;

int solve() {
    int limit = 600;
    vector<int> dp(limit + 1, 1000);  // dp[i]: number of coins
    dp[0] = 0;

    for (int i = 0; i < 6; i ++) {
        for (int j = nums[i]; j >= 1; j --) {
            for (int k = limit; k >= value[i]; k --) {
                dp[k] = min(dp[k], 1 + dp[k - value[i]]);
            }
        }
    }

    vector<int> exchange(200);
    for (int i = 5; i <= 200; i ++) {
        int remain = i;
        for (int k = 5; k >= 0 && remain; --k) {
            exchange[i] += remain / value[k];
            remain %= value[k];
        }
    }

    int ans = INT_MAX;
    for (int i = limit; i >= target; i --) {
        if (dp[i] < 1000) {
            ans = min(ans, dp[i] + exchange[i - target]);
        }
    }
    return ans;
}

int main() {
    value = {5, 10, 20, 50, 100, 200};
    while (cin >> nums[0] >> nums[1] >>
           nums[2] >> nums[3] >> nums[4] >> nums[5]) {
        s = nums[0] + nums[1] + nums[2] +
            nums[3] + nums[4] + nums[5];
        if (s == 0) {
            break;
        }

        cin >> temp_target;
        target = static_cast<int>(temp_target * 100);

        cout << solve() << endl;
    }

    return 0;
}
