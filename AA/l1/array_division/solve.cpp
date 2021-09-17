#pragma GCC optimize("Ofast,no-stack-protector")

#include <map>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
#include <limits.h>
#include <bits/stdc++.h>
#include <numeric>



using namespace std;

long long ans;
vector<long long> nums(200001);
long long N, T, K;

bool cal(long long target) {
    long long curr = nums[0];
    if(nums[0] > target) return false;
    long long cnt = 1;
    for(long long i = 1; i < N; i++) {
        if(curr + nums[i] <= target) {
            curr += nums[i];
        } else {
            if(nums[i] > target) return false;
            curr = nums[i];
            cnt += 1;
        }
    }
    if(cnt > K) {return false;}
    return true;
}

void solve() {
    long long l = (long long) *std::max_element(nums.begin(), nums.end());
    long long r = LLONG_MAX;

    while(l < r) {
        long long mid = l + (r - l) / 2;
        if(cal(mid)) {
            r = mid;
        } else {
            l = mid + 1;
        }
    }
    cout << l << endl;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);

    cin >> N >> K;
    for(long long i = 0; i < N; i++) {
        cin >> nums[i];
    }
    solve();
}
