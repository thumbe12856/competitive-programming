#pragma GCC optimize("Ofast,no-stack-protector")

#include <map>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
#include <limits.h>
#include <bits/stdc++.h>

using namespace std;

vector<long long> nums(20);
long long ans;
int N;


long long dfs(long long s, long long curr_s, int idx) {
    if(idx == N) {
        return abs(s - curr_s - curr_s);
    }

    return min(
        dfs(s, curr_s, idx + 1),
        dfs(s, curr_s + nums[idx], idx + 1)
    );
}

void solve() {
    long long s = 0;
    for(auto n : nums) {
        s += n;
    }
    cout << dfs(s, 0, 0) << endl;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);

    cin >> N;
    for(int i = 0; i < N; i ++) {
        cin >> nums[i];
    }

    solve();
}
