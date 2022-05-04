#pragma GCC optimize("Ofast,no-stack-protector")

#include <map>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
#include <limits.h>
#include <bits/stdc++.h>
#include <math.h>

using namespace std;

long long x, y;

long long solve(long long n) {
    long long ans = 0;

    for(long long i = 1; i * i <= n; i++) {
        ans += (n / i - i) * 2 + 1;
    }

    cout << ans << endl;
    return ans;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> x >> y;
    cout << solve(y) - solve(x - 1) << endl;
}
