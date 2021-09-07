#pragma GCC optimize("Ofast,no-stack-protector")

#include <map>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
#include <limits.h>
#include <bits/stdc++.h>
# include <cstdio>

using namespace std;

int N, T;

void solve(vector<int>& nums) {
    vector<int> nums2 = nums;
    sort(nums2.begin(), nums2.end());
    nums2.resize(unique(nums2.begin(), nums2.end()) - nums2.begin());

    int cnt = 0;
    for(int i = 0; i < N; i++) {
        auto idx = lower_bound(nums2.begin(), nums2.end(), nums[i]) - nums2.begin();
        cout << idx + 1 << " ";
    }
    cout << endl;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);

    cin >> T;
    for(int i = 0; i < T; i ++) {
        cin >> N;
        vector<int> nums(N);
        for(int j = 0; j < N; j++) {
            cin >> nums[j];
        }

        solve(nums);
    }
}
