#include <map>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
#include <limits.h>
#include <bits/stdc++.h>

using namespace std;

std::set<int> ans;
std::set<int> vis;
vector<vector<int>> G(200001);
vector<int> C(200001);
vector<int> cnt(200001);

void dfs(int node) {
    if(cnt[C[node - 1]] == 0) {
        ans.insert(node);
    }

    vis.insert(node);
    cnt[C[node - 1]] += 1;
    for(auto next_node : G[node]) {
        if(vis.find(next_node) != vis.end()) {
            continue;
        }
        dfs(next_node);
    }
    cnt[C[node - 1]] -= 1;
    vis.erase(node);
}

void solve() {
    dfs(1);
    for(auto node : ans) {
        cout << node << endl;
    }
}

int main() {
    int N, f, t;
    cin >> N;
    for(int i = 0; i < N; i ++) {
        cin >> C[i];
    }

    for(int i = 0; i < N - 1; i ++) {
        cin >> f >> t;
        G[f].push_back(t);
        G[t].push_back(f);
    }
    solve();
}
