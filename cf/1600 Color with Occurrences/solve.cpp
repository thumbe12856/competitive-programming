#pragma GCC optimize("Ofast,no-stack-protector")

#include <bits/stdc++.h>
#include <limits.h>

#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <vector>

using namespace std;

void solve(string &s, vector<string> &can) {
    int right = 0;
    int ans = 0;
    vector<int> dp(s.size(), INT_MAX);
    vector<pair<int, int>> path(s.size());
    for (int i = 0; i < s.size(); i++) {
        int max_k = 0;
        int p_k = 0;
        for (int j = 0; j < can.size(); j++) {
            bool valid = true;
            for (int k = 0; k < can[j].size(); k++) {
                if (k + i >= s.size()) {
                    valid = false;
                    break;
                }
                if (s[k + i] != can[j][k]) {
                    valid = false;
                    break;
                }
            }

            if (valid && can[j].size() > max_k) {
                max_k = can[j].size();
                p_k = j;
            }
        }

        bool set_path = false;
        int prev = 0;
        if (i != 0) {
            prev = dp[i - 1];
        }

        if (prev + 1 < dp[i + max_k - 1]) {
            set_path = true;
        }

        for (int q = i; q < i + max_k; q++) {
            if (prev + 1 <= dp[q]) {
                dp[q] = prev + 1;
            }

            if (set_path) {
                path[q] = {p_k + 1, i + 1};
            }
        }
    }

    if (dp[s.size() - 1] != INT_MAX) {
        cout << dp[s.size() - 1] << endl;
        int i = 0;
        while (i < path.size()) {
            cout << path[i].first << " " << path[i].second << endl;
            i = path[i].second - 1 + can[path[i].first - 1].size();
        }
    } else {
        cout << -1 << endl;
    }
}

int main() {
    int T, N;
    string s;
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> T;
    for (int i = 0; i < T; i++) {
        cin >> s;
        cin >> N;
        vector<string> can(N);
        for (int n = 0; n < N; n++) {
            cin >> can[n];
        }
        solve(s, can);
    }
    return 0;
}
