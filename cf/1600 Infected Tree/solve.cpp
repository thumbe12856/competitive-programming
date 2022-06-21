#pragma GCC optimize("Ofast,no-stack-protector")

#include <map>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
#include <limits.h>
#include <bits/stdc++.h>

using namespace std;

std::set<int> vis;
std::set<int> can;
unordered_map<int, set<int>> G;
int T, N, f, t;


int dfs(int parent, int node) {
    if (G[node].size() == 1) {
        return 0;
    }

    if (G[node].size() == 2) {
        return 1;
    }

    int res = LONG_LONG_MAX;
    for (auto& next_node : G[node]) {
        if (next_node == parent) {
            continue;
        }

        res = min(res, dfs(node, next_node));
    }
    return res + 2;
}

int solve() {
    if (N == 2) {
        return 0;
    }

    return N - dfs(0, 1) - 1;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> T;
    for (int tt = 0; tt < T; tt ++) {
        cin >> N;
        for (int i = 0; i < N - 1; i ++) {
            cin >> f >> t;
            G[f].insert(t);
            G[t].insert(f);
        }
        G[1].insert(0);

        cout << solve() << endl;
        G.clear();
    }

    solve();
}
