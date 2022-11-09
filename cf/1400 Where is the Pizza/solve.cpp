#pragma GCC optimize("Ofast,no-stack-protector")

#include <bits/stdc++.h>
#include <limits.h>

#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <vector>

using namespace std;

int solve(int N, map<int, int> &G, vector<int> &keys, map<int, int> &D) {
    map<int, int> vis;
    for (int i = 0; i < N; i++) {
        vis[keys[i]] = -1;
    }

    for (int i = 0; i < N; i++) {
        int f = keys[i];
        vector<int> group;
        bool fixed = false;
        while (vis[f] == -1) {
            int t = G[f];
            vis[f] = 1;
            if (f != t) {
                group.push_back(f);
                if (D[f] != 0) {
                    fixed = true;
                }
            }
            f = t;
        }

        if (!fixed && !group.empty()) {
            vis[group[0]] = 2;
        }
    }

    int ans = 1;
    for (int i = 1; i <= N; i++) {
        ans = (ans * vis[i]) % 1000000007;
    }
    return ans;
}

int main() {
    int T, N, f, t;
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> T;
    for (int i = 0; i < T; i++) {
        cin >> N;
        map<int, int> G;
        vector<int> keys(N);
        map<int, int> D;
        for (int j = 0; j < N; j++) {
            cin >> keys[j];
        }
        for (int j = 0; j < N; j++) {
            cin >> G[keys[j]];
        }
        for (int j = 0; j < N; j++) {
            cin >> D[keys[j]];
        }
        cout << solve(N, G, keys, D) << endl;
    }
    return 0;
}
