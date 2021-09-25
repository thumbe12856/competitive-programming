#pragma GCC optimize("Ofast,no-stack-protector")

#include <map>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
#include <limits.h>
#include <bits/stdc++.h>

using namespace std;

int N, K, f, t;

void solve(vector<pair<int, int>>& nums) {
    // sort by movie's end time
    sort(
        nums.begin(),
        nums.end(),
        [](const pair<int, int>& n1, const pair<int, int>& n2) {
            return n1.second < n2.second;
        }
    );

    multiset<int> q;
    for(int i = 0; i < K; i++) {
        q.insert(0);
    }

    int ans = 0;
    for(int i = 0; i < N; i++) {
        auto it = q.upper_bound(nums[i].first);
        if(it == q.begin()) {
            continue;
        }

        it--;
        q.erase(it);
        q.insert(nums[i].second);

        ans ++;
    }

    cout << ans << endl;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);

    cin >> N >> K;
    vector<pair<int, int>> nums(N);
    for(int i = 0; i < N; i ++) {
        cin >> nums[i].first >> nums[i].second;
    }

    solve(nums);
}
