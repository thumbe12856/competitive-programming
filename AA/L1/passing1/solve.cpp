#include <map>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
#include <limits.h>
#include <bits/stdc++.h>
#include <stdio.h>

using namespace std;

vector<int> ans(200001);
std::set<int> vis;
vector<vector<int>> G(200001);
vector<vector<std::pair<int, int>>> q(200001);
int N, Q, f, t, x, y;

void dfs(int node) {
    vis.insert(node);

    for(int i = 0; i < q[node].size(); i ++) {
        auto x = q[node][i].first;
        auto idx = q[node][i].second;
        if(vis.find(x) != vis.end()) {
            ans[idx] = 1;
        }
    }

    for(auto next_node : G[node]) {
        if(vis.find(next_node) != vis.end()) {
            continue;
        }
        dfs(next_node);
    }

    vis.erase(node);
}

void solve() {
    dfs(1);
    for(int i = 0; i < Q; i ++) {
        cout << ans[i] << endl;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.precision(20);

    cin >> N;
    for(int f = 0; f < N - 1; f ++) {
        cin >> t;
        G[f + 2].emplace_back(t);
        G[t].emplace_back(f + 2);
    }

    cin >> Q;
    for(int i = 0; i < Q; i ++) {
        cin >> x >> y;
        q[y].emplace_back(std::make_pair(x, i));
    }
    solve();
}
