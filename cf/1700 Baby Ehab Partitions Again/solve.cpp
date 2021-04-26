#include <map>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
#include <limits.h>
#include <bits/stdc++.h>

using namespace std;

void solve(int N, int* nums) {
    int i, j, k;
    int total = 0;
    bitset<2000001> dp;
    dp[0] = 1;
    int cnt = 100;
    int temp_cnt;
    int res = -1;

    for(i = 0; i < N; i++) {
        total += nums[i];
        dp |= (dp << nums[i]);

        temp_cnt = __builtin_ctz(nums[i]);
        if(temp_cnt < cnt) {
            cnt = temp_cnt;
            res = i;
        }
    }

    if(total & 1 || dp[total / 2] == 0) {
        cout << 0 << endl;
        return;
    }

    cout << 1 << endl;
    cout << res + 1 << endl;
    return;
}

int main() {
    int T, N, K;
    int i, j, k;
    int nums[101];

    cin >> N;
    for(i = 0; i < N; i++) {
        int temp;
        cin >> nums[i];
    }
    solve(N, nums);

}
