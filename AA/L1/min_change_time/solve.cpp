#pragma GCC optimize("Ofast,no-stack-protector")

#include <map>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
#include <limits.h>
#include <bits/stdc++.h>

using namespace std;

long long ans;
int nums[500000];
int next_nums[500000];
int N;

long long dfs(int l, int r) {
    if(l + 1 >= r) {
        return 0;
    }

    int mid = l + (r - l) / 2;
    long long res = dfs(l, mid) + dfs(mid, r);
    int curr_l = l;
    int curr_r = mid;
    int idx = 0;
    while(curr_l < mid || curr_r < r) {
        if(curr_r == r || (curr_l < mid && nums[curr_l] <= nums[curr_r])) {
            res += curr_r - mid;
            next_nums[idx++] = nums[curr_l++];
        } else {
            next_nums[idx++] = nums[curr_r++];
        }
    }

    memcpy(nums + l, next_nums, (r - l) * sizeof(int));
    return res;
}

long long solve() {
    return dfs(0, N);
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);

    cin >> N;
    for(int i = 0; i < N; i ++) {
        cin >> nums[i];
    }

    cout << solve() << endl;
}
