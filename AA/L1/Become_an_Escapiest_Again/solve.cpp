#pragma GCC optimize("Ofast,no-stack-protector")

#include <map>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
#include <limits.h>
#include <bits/stdc++.h>

using namespace std;

const int SIZE = 1000;
int vis[SIZE][SIZE][2];
int G[SIZE][SIZE];
vector<pair<int, int>> dirs;
int N, Q, f, t, x, y;

void solve() {
    vector<pair<int, int>> q1;
    vector<pair<int, int>> q2;
    q1.push_back(make_pair(0, 0));
    q2.push_back(make_pair(1, 0));
    q1.push_back(make_pair(0, 0));
    q2.push_back(make_pair(1, 1));

    while(q1.size() > 0) {
        vector<pair<int, int>> next_q1;
        vector<pair<int, int>> next_q2;

        for(int idx = 0; idx < q1.size(); idx++) {
            auto i = q1[idx].first;
            auto j = q1[idx].second;
            auto d = q2[idx].first;
            auto f = q2[idx].second;

            if(i == N - 1 && j == N - 1) {
                cout << d << endl;
                return;
            }

            if(vis[i][j][f] == 1) {
                continue;
            }

            vis[i][j][f] = 1;
            auto curr_val = G[i][j];
            for(auto dd : dirs) {
                auto x = dd.first, y = dd.second;
                if(0 <= i + x && i + x < N &&
                   0 <= j + y && j + y < N) {
                        auto next_val = G[i + x][j + y];
                        auto valid = false;

                        if(f == 0 && next_val > curr_val) {
                            valid = true;
                        } else if(f == 1 && next_val < curr_val) {
                            valid = true;
                        }

                        if(valid) {
                            next_q1.push_back(make_pair(i + x, j + y));
                            next_q2.push_back(make_pair(d + 1, 1 - f));
                        }
                   }
            }
        }

        q1 = next_q1;
        q2 = next_q2;
    }


    cout << -1 << endl;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);

    dirs.push_back(make_pair(0, 1));
    dirs.push_back(make_pair(1, 0));
    dirs.push_back(make_pair(0, -1));
    dirs.push_back(make_pair(-1, 0));

    cin >> N;
    for(int i = 0; i < N; i ++) {
        for(int j = 0; j < N; j ++) {
            cin >> G[i][j];
        }
    }

    solve();
}
