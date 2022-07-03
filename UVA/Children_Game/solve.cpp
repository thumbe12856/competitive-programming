#pragma GCC optimize("Ofast,no-stack-protector")

#include <map>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
#include <limits.h>
#include <bits/stdc++.h>

using namespace std;

bool compare(const string& s1, const string& s2) {
    return s1 + s2 < s2 + s1;
}

int main() {
    int N;
    while (cin >> N) {
        if (N == 0) {
            break;
        }

        vector<string> nums(N);
        for (int i = 0; i < N; i ++) {
            cin >> nums[i];
        }

        for (int i = 0; i < N; i ++) {
            for (int j = i + 1; j < N; j ++) {
                if (compare(nums[i], nums[j])) {
                    swap(nums[i], nums[j]);
                }
            }
        }

        for (int i = 0; i < N; i ++) {
            cout << nums[i];
        }
        cout << endl;
    }

    return 0;
}
