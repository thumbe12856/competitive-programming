// Copyright 2022 edward

#include <map>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
#include <limits.h>
#include <bits/stdc++.h>

using namespace std;


int solve(int M, int N, const vector<string>& G, int x, int y) {
    char target = G[x][y];
    int ans = 0;
    int size = 1;
    bool valid = true;

    while (valid) {
        for (int i = x - size; i <= x + size; i ++) {
            for (int j = y - size; j <= y + size; j ++) {
                if (!(0 <= i && i < M && 0 <= j && j < N)) {
                    valid = false;
                    break;
                }

                if (G[i][j] != target) {
                    valid = false;
                    break;
                }
            }

            if (!valid) {
                break;
            }
        }

        if (valid) {
            ans = size;
        }
        size++;
    }

    return ans * 2 + 1;
}

int main() {
    int T, M, N, Q, x, y;

    cin >> T;
    for (int i = 0; i < T; i ++) {
        vector<string> G;
        cin >> M >> N >> Q;
        cout << M << " " << N << " " << Q << endl;
        for (int j = 0; j < M; j ++) {
            string s;
            cin >> s;
            G.push_back(s);
        }

        for (int j = 0; j < Q; j ++) {
            cin >> x >> y;
            cout << solve(M, N, G, x, y) << endl;
        }
    }
}
