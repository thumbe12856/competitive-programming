#pragma GCC optimize("Ofast,no-stack-protector")

#include <map>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
#include <limits.h>
#include <bits/stdc++.h>

using namespace std;

std::set<int> vis_node;
int vis[2001][2];
vector<vector<pair<int, int>>> G(2001);
int N, M, a, b, c;


void dfs(int node, int mud) {
    if(vis[node][mud]) {
        return;
    }

    vis[node][mud] = 1;
    vis_node.insert(node);
    for(auto p : G[node]) {
        if(p.second == 0) {
            dfs(p.first, mud);
        } else {
            if(mud) {
                dfs(p.first, 0);
            }
        }
    }
}

void solve() {
    int ans = 0;
    for(int i = 1; i <= N; i++) {
        memset(&vis, 0, sizeof(vis));
        vis_node.clear();
        dfs(i, 1);
        ans += vis_node.size();
    }

    cout << ans << endl;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);
    cin >> N >> M;
    for(int i = 0; i < M; i ++) {
        cin >> a >> b >> c;
        G[a].push_back(make_pair(b, c));
    }

    solve();
}
