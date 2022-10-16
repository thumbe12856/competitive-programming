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

int solve(int N, int K, string& S) {
  int first = -1;
  int last = -1;

  for (int i = N - 1; i >= 0; i --) {
    if (S[i] == '1') {
      if (K >= N - 1 - i) {
        K -= N - 1 - i;
        swap(S[N - 1], S[i]);
      }
      break;
    }
  }

  for (int i = 0; i < N; i ++) {
    if (S[i] == '1') {
      if (K >= i && i != N - 1) {
        swap(S[0], S[i]);
      }
      break;
    }
  }

  int ans = 0;
  for (int i = 0; i < N - 1; i ++) {
    ans += (S[i] - '0') * 10 + S[i + 1] - '0';
  }

  return ans;
}

int main() {
  int N, K, T;
  string S;

  ios::sync_with_stdio(0);
  cin.tie(0);cout.tie(0);
  cin >> T;
  for(int i = 0; i < T; i ++) {
    cin >> N >> K;
    cin >> S;
    cout << solve(N, K, S) << endl;
  }

  return 0;
}
