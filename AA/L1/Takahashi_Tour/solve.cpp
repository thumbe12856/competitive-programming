#include <map>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
#include <limits.h>
#include <bits/stdc++.h>

using namespace std;

vector<int> ans;
std::set<int> vis;
vector<vector<int>> G(200001);

void dfs(int node) {
    ans.push_back(node);
    vis.insert(node);
    for(auto next_node : G[node]) {
        if(vis.find(next_node) != vis.end()) {
            continue;
        }
        dfs(next_node);
        ans.push_back(node);
    }
}

void solve() {
    for(int f = 1; f < G.size(); f++) {
        std::sort(std::begin(G[f]), std::end(G[f]));
    }

    dfs(1);
    for(auto node : ans) {
        cout << node << " ";
    }
    cout << endl;
}

int main() {
    int N, f, t;
    cin >> N;

    for(int i = 0; i < N - 1; i ++) {
        cin >> f >> t;
        G[f].push_back(t);
        G[t].push_back(f);
    }
    solve();
}
