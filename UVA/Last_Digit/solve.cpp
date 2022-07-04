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
    vector<int> table = {0};
    int val = 0;
    for (int i = 1; i < 20; i ++) {
        int temp = 1;
        for (int j = 0; j < i; j ++) {
            temp = temp * i % 10;
        }

        val = (val + temp) % 10;
        table.push_back(val);
    }

    string N;
    while (cin >> N) {
        if (N == "0") {
            break;
        }

        int n = 0;
        for (int i = max(0, (int) N.size() - 2); i < N.size(); i ++) {
            n *= 10;
            n += N[i] - '0';
        }

        cout << (table[n % 20] + n / 20 * table.back()) % 10 << endl;
    }

    return 0;
}
