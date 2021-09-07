#pragma GCC optimize("Ofast,no-stack-protector")

#include <map>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
#include <limits.h>
#include <bits/stdc++.h>

using namespace std;

int L, R, V1, V2;

int d_sum(int d) {
    int res = 0;
    while(d) {
        res += d % 10;
        d /= 10;
    }
    return res;
}

long long solve(int L, int R, int V) {
    long long ans = 0;
    int s = 0;

    int l = L;
    int r = L;
    while(r <= R) {
        s += d_sum(r);
        while(s > V) {
            s -= d_sum(l);
            l += 1;
        }
        ans += r - l + 1;
        r += 1;
    }

    return ans;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);

    cin >> L >> R >> V1 >> V2;
    cout << solve(L, R, V2) - solve(L, R, V1 - 1);
}
