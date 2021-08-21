#include <map>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
#include <limits.h>
#include <bits/stdc++.h>

using namespace std;

unsigned long long solve(unsigned long long A, unsigned long long D, unsigned long long N) {
    unsigned long long ans = 0;
    unsigned long long target = A + N * D;
    for(unsigned long long n = A; n < target; n += D) {
        ans += n + n - __builtin_popcountll(n);
    }
    return ans;
}

int main() {
    unsigned long long A, D, N;
    cin >> A >> D >> N;
    cout << solve(A, D, N) << endl;
}
