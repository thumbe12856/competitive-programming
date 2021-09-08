#pragma GCC optimize("Ofast,no-stack-protector")

#include <map>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
#include <limits.h>
#include <bits/stdc++.h>

using namespace std;

int N;

long long int solve(vector<int>& ori_nums) {
    auto nums = ori_nums;
    long long int ans = 0;
    int i;
    for(i = 1; i < N; i++) {
        nums[i] -= i + nums[0];
    }
    nums[0] = 0;
    sort(nums.begin(), nums.end());
    long long int cnt = 1;
    for(i = 1; i < N; i++) {
        if(nums[i] == nums[i - 1]) {
            cnt += 1;
        } else {
            ans += (cnt) * (cnt - 1) / 2;
            cnt = 1;
        }
    }
    ans += (cnt) * (cnt - 1) / 2;

    return ans * 2;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);

    cin >> N;
    vector<int> nums(N);
    for(int i = 0; i < N; i ++) {
        cin >> nums[i];
    }

    long long int ans = solve(nums);
    reverse(nums.begin(), nums.end());
    ans += solve(nums);
    cout << ans << endl;
}
