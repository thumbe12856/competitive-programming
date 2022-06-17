#include <map>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
#include <limits.h>
#include <bits/stdc++.h>

using namespace std;

void dfs(vector<string>& G, char target, int x, int y) {
    if (!(0 <= x && x < G.size() &&
          0 <= y && y < G[0].size())) {
        return;
    }

    if (G[x][y] == '.' || G[x][y] != target) {
        return;
    }

    G[x][y] = '.';
    dfs(G, target, x + 1, y);
    dfs(G, target, x, y + 1);
    dfs(G, target, x - 1, y);
    dfs(G, target, x, y - 1);
}

void solve(int M, int N, vector<string>& G) {
    map<char, int> vis;
    for (int i = 0; i < M; i ++) {
        for (int j = 0; j < N; j ++) {
            char c = G[i][j];
            if (c == '.') {
                continue;
            }

            dfs(G, c, i, j);
            vis[c] += 1;
        }
    }

    while (vis.size()) {
        int max_time = -1;
        char c = (char)((int)'z' + 1);

        for (auto pair: vis) {
            if (pair.second > max_time) {
                c = pair.first;
                max_time = pair.second;
            } else if (pair.second == max_time && pair.first < c) {
                c = pair.first;
                max_time = pair.second;
            }
        }

        cout << c << ": " << max_time << endl;
        vis.erase(c);
    }
}

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t ++) {
        cout << "World #" << t + 1 << endl;

        int M, N;
        vector<string> G;
        cin >> M >> N;
        for (int j = 0; j < M; j ++) {
            string s;
            cin >> s;
            G.push_back(s);
        }

        solve(M, N, G);
    }
}
