#pragma GCC optimize("Ofast,no-stack-protector")

#include <map>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
#include <limits.h>
#include <bits/stdc++.h>

using namespace std;

vector<int> nums(200001);
int N;

void solve() {
    long long int ans = 0;

    for(int i = 1; i < N - 1; i ++) {
        int j = i - 1;
        int k = i + 1;
        auto target = nums[i] * 2;
        while(j >= 0 && k < N) {
            if(nums[j] + nums[k] >= target) {
                j -= 1;
            } else {
                ans += j + 1;
                k += 1;
            }
        }
    }

    cout << ans << endl;
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
