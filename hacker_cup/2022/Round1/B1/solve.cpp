#pragma GCC optimize("Ofast,no-stack-protector")

#include <map>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
#include <limits.h>
#include <bits/stdc++.h>

using namespace std;

long long T, N, M;
long long MOD = 1000000007;

template <typename T>
T modpow(T base, T exp, T modulus) {
  base %= modulus;
  T result = 1;
  while (exp > 0) {
    if (exp & 1) result = (result * base) % modulus;
    base = (base * base) % modulus;
    exp >>= 1;
  }
  return result;
}

long long solve(map<long long, long long>& tree, map<long long, long long>& well) {
  long long res = 0;
  for (auto t : tree) {
    for (auto w : well) {
      long long diff = abs(t.first - w.first);
      res += modpow(diff, (long long) 2, MOD) * (t.second * w.second);
    }
  }

  return res;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);

    cin >> T;
    long long x, y;
    for(long long i = 0; i < T; i ++) {
      map<long long, long long> tree_x;
      map<long long, long long> tree_y;
      map<long long, long long> well_x;
      map<long long, long long> well_y;

      cin >> N;
      for (long long j = 0; j < N; j ++) {
        cin >> x >> y;
        tree_x[x] += 1;
        tree_y[y] += 1;
      }

      cin >> M;
      for (long long j = 0; j < M; j ++) {
        cin >> x >> y;
        well_x[x] += 1;
        well_y[y] += 1;
      }

      long long ans = (solve(tree_x, well_x) + solve(tree_y, well_y)) % MOD;
      cout << "Case #" << i + 1 << ": " << ans << endl;
    }
}
