#pragma GCC optimize("Ofast,no-stack-protector")

#include <bits/stdc++.h>
#include <limits.h>

#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <vector>

using namespace std;

void dfs(int node, map<int, vector<int>> &G, map<pair<int, int>, int> &order, vector<int> &weight, int parent, int parent_weight) {
    for (int i = 0; i < G[node].size(); i++) {
        int child = G[node][i];
        pair<int, int> key = {min(child, node), max(child, node)};
        if (child != parent && weight[order[key]] == -1) {
            parent_weight = 5 - parent_weight;
            weight[order[key]] = parent_weight;
            dfs(child, G, order, weight, node, parent_weight);
        }
    }
}

void solve(int N, map<int, vector<int>> &G, map<pair<int, int>, int> &order) {
    vector<int> weight(N - 1, -1);
    for (int j = 1; j <= N; j++) {
        if (G[j].size() > 2) {
            cout << "-1" << endl;
            return;
        }
    }

    for (int j = 1; j <= N; j++) {
        dfs(j, G, order, weight, -1, 3);
    }

    for (int j = 0; j < N - 1; j++) {
        cout << weight[j] << " ";
    }
    cout << endl;
}

int main() {
    int T, N, f, t;
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> T;
    for (int i = 0; i < T; i++) {
        cin >> N;
        map<int, vector<int>> G;
        map<pair<int, int>, int> order;
        for (int j = 0; j < N - 1; j++) {
            cin >> f >> t;
            G[f].push_back(t);
            G[t].push_back(f);
            order[{min(f, t), max(f, t)}] = j;
        }
        solve(N, G, order);
    }
    return 0;
}
