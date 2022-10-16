#pragma GCC optimize("Ofast,no-stack-protector")

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
vector<vector<std::pair<int, int>>> q(200001);
vector<pair<int, int>> dirs;

string solve(int M, int N, vector<vector<int>>& grid) {
  vector<int> last_diff;

  for (int i = 0; i < M; i ++) {
    vector<int> temp;
    temp.assign(grid[i].begin(), grid[i].end());
    sort(temp.begin(), temp.end());

    vector<int> diff;
    for (int j = 0; j < N; j ++) {
      if (temp[j] != grid[i][j]) {
        diff.push_back(j);
      }
    }

    if (diff.size() > 2) {
      return "-1";
    }

    if (!diff.empty()) {
      if (last_diff.size() == 0) {
        last_diff = diff;
      } else {
        if (last_diff != diff) {
          return "-1";
        }
      }
    }
  }

  if (last_diff.size() == 0) {
    return "1 1";
  }

  for (int i = 0; i < M; i ++) {
    swap(grid[i][last_diff[0]], grid[i][last_diff[1]]);
    for (int j = 0; j < N - 1; j ++) {
      if (grid[i][j] > grid[i][j + 1]) {
        return "-1";
      }
    }
  }

  return to_string(last_diff[0] + 1) + " " + to_string(last_diff[1] + 1);
}

int main() {
  int T, M, N;
  string S;

  ios::sync_with_stdio(0);
  cin.tie(0);cout.tie(0);
  cin >> T;
  while (T --) {
    cin >> M >> N;
    vector<vector<int>> grid(M, vector<int>(N, 0));
    for (int i = 0; i < M; i ++) {
      for (int j = 0; j < N; j ++) {
        cin >> grid[i][j];
      }
    }
    cout << solve(M, N, grid) << endl;
  }

  return 0;
}
