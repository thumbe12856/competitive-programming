#pragma GCC optimize("Ofast,no-stack-protector")

#include <map>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
#include <limits.h>
#include <bits/stdc++.h>

using namespace std;

long long int C[101];
long long int dp[1000001];
int N, target;
const int MOD = 1000000007;

void solve() {

    sort(C, C + N);

    dp[0] = 1;
    for(int i = 1; i <= target; i++) {
        for(int j = 0; j < N; j++) {
            auto c = C[j];
            if(c > i) {
                break;
            }

            dp[i] += dp[i - c] % MOD;
        }
    }

    cout << dp[target] % MOD << "\n";
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);

    cin >> N >> target;
    for(int i = 0; i < N; i ++) {
        cin >> C[i];
    }

    solve();
}
