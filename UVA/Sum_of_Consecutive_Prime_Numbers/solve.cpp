#pragma GCC optimize("Ofast,no-stack-protector")

#include <map>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
#include <limits.h>
#include <bits/stdc++.h>

using namespace std;

int main() {
    int limit = 10000;
    vector<int> table(limit + 1);
    vector<int> primes;
    for (int i = 2; i <= limit; i ++) {
        if (table[i] == 1) {
            continue;
        }

        primes.push_back(i);
        for (int j = i; j <= limit; j += i) {
            table[j] = 1;
        }
    }

    vector<int> presum = {0};
    for (int i = 0; i < primes.size(); i ++) {
        presum.push_back(presum.back() + primes[i]);
    }

    int N;
    while (cin >> N) {
        if (N == 0) {
            break;
        }

        int ans = 0;
        for (int i = 0; i < presum.size(); i ++) {
            for (int j = 0; j < i; j ++) {
                int val = presum[i] - presum[j];
                if (val == N) {
                    ans += 1;
                }
            }
        }
        cout << ans << endl;
    }

    return 0;
}
