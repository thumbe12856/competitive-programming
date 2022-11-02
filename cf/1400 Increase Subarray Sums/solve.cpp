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

string solve(vector<int>& nums, int X, int N) {
  string ans = "";
  vector<int> mx(N + 1, -INT_MAX);
  for (int i = 0; i < N; i ++) {
    int current_sum = 0;
    for (int j = i; j < N; j ++) {
      current_sum += nums[j];
      mx[j - i + 1] = max(mx[j - i + 1], current_sum);
    }
  }

  for (int k = 0; k <= N; k ++) {
    int curr = 0;
    for (int l = 0; l <= N; l ++) {
      curr = max(curr, mx[l] + min(k, l) * X);
    }
    ans += to_string(curr) + (k == N ? "" : " ");
  }

  return ans;
}

int main() {
  int T, N, X;

  ios::sync_with_stdio(0);
  cin.tie(0);cout.tie(0);
  cin >> T;
  while (T --) {
    cin >> N >> X;
    vector<int> nums(N);
    for (int i = 0; i < N; i ++) {
      cin >> nums[i];
    }
    cout << solve(nums, X, N) << endl;
  }

  return 0;
}
