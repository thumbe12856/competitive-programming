#pragma GCC optimize("Ofast,no-stack-protector")

#include <map>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
#include <limits.h>
#include <bits/stdc++.h>
#include <stdio.h>

using namespace std;

int nums[25];
int N, val;
unordered_map<int, int> can;
map<tuple<int, int, int>, int> vis;
// map<tuple<int, int>, int> vis;
int ans = INT_MAX;


int dfs(int idx, int curr, int curr_res) {
    auto key = std::tuple(idx, curr, curr_res);

    if(idx >= N) {
        if(curr_res < ans) {
            ans = curr_res;
        }

        vis[key] = curr_res;
        return curr_res;
    }

    if(curr_res >= ans) {
        vis[key] = INT_MAX;
        return INT_MAX;
    }

    if(vis.find(key) != vis.end()) {
        return vis[key];
    }

    auto val = curr + nums[idx];
    int res1, res2;
    can[val] += 1;
    if(can[val] == 1) {
        res1 = dfs(idx + 1, val, curr_res + 1);
    } else {
        res1 = dfs(idx + 1, val, curr_res);
    }
    can[val] -= 1;

    val = curr - nums[idx];
    can[val] += 1;
    if(can[val] == 1) {
        res2 = dfs(idx + 1, val, curr_res + 1);
    } else {
        res2 = dfs(idx + 1, val, curr_res);
    }
    can[val] -= 1;
    auto res = min(res1, res2);
    ans = min(ans, res);

    vis[key] = res;
    return res;
}

int main() {
    cin >> N;
    for(int i = 0; i < N; i ++) {
        cin >> nums[i];
    }

    can[0] = 1;
    cout << dfs(0, 0, 1) << endl;
    // cout << vis.size();

    return 0;
}
