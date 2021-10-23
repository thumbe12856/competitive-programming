#pragma GCC optimize("Ofast,no-stack-protector")

#include <map>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
#include <limits.h>
#include <bits/stdc++.h>

using namespace std;

int ans;
vector<vector<char>> G(1001);
vector<pair<int, int>> dirs;
int N, M;

void dfs(int i, int j) {
    if(!(0 <= i && i < M && 0 <= j && j < N)) {
        return;
    }

    if(G[i][j] != '.') {
        return;
    }

    G[i][j] = '#';
    for(auto d : dirs) {
        dfs(i + d.first, j + d.second);
    }
}

void solve() {
    ans = 0;

    for(int i = 0; i < M; i ++) {
        for(int j = 0; j < N; j ++) {
            if(G[i][j] == '.') {
                ans += 1;
                dfs(i, j);
            }
        }
    }

    cout << ans << endl;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);

    dirs.push_back(make_pair(0, 1));
    dirs.push_back(make_pair(1, 0));
    dirs.push_back(make_pair(0, -1));
    dirs.push_back(make_pair(-1, 0));

    cin >> M >> N;
    for(int i = 0; i < M; i ++) {
        for(int j = 0; j < N; j ++) {
            char c;
            cin >> c;
            G[i].push_back(c);
        }
    }

    solve();
}
