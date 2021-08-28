#include <map>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
#include <limits.h>
#include <bits/stdc++.h>

using namespace std;


vector<int> ans(200001);
std::set<int> vis;
std::set<int> can;
vector<vector<int>> G(200001);
vector<pair<int, int>> q[200001];
int int_the_way[200001] = {0};

int N, Q, f, t, x, y;

// TLE
void dfs(int node) {
    vis.insert(node);
    for(auto next_node : G[node]) {
        can.insert(next_node);
    }

    for(int i = 0; i < q[node].size(); i ++) {
        auto x = q[node][i].first;
        auto idx = q[node][i].second;
        if(can.find(x) != can.end()) {
            ans[idx] = 1;
        }
    }

    for(auto next_node : G[node]) {
        if(vis.find(next_node) != vis.end()) {
            continue;
        }
        dfs(next_node);
    }

    for(auto next_node : G[node]) {
        if(vis.find(next_node) != vis.end()) {
            continue;
        }
        can.erase(next_node);
    }
    vis.erase(node);
}

// dealing with int array is much faster than set
void dfs2(int node) {
    int_the_way[node]++;
    for(auto next_node : G[node]) {
        int_the_way[next_node]++;
    }

    for(int i = 0; i < q[node].size(); i ++) {
        auto x = q[node][i].first;
        auto idx = q[node][i].second;
        ans[idx] = int_the_way[x] ? 1 : 0;
    }

    for(auto next_node : G[node]) {
        if(int_the_way[next_node] == 1) {
            dfs2(next_node);
        }
    }

    int_the_way[node]--;
    for(auto next_node : G[node]) {
        int_the_way[next_node]--;
    }
}

void solve() {
    // dfs(1);
    dfs2(1);
    for(int i = 0; i < Q; i ++) {
        cout << ans[i] << endl;
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);

    cin >> N;
    for(int i = 0; i < N - 1; i ++) {
        cin >> f >> t;
        G[f].emplace_back(t);
        G[t].emplace_back(f);
    }

    cin >> Q;
    for(int i = 0; i < Q; i ++) {
        cin >> x >> y;
        q[y].push_back({x, i});
    }
    solve();
}
