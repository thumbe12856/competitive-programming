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
    ios::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);
    int N, M, n, i, j;
    cin >> N >> M;

    multiset<int> nums;
    for(i = 0; i < N; i ++) {
        cin >> n;
        nums.insert(n);
    }

    for(i = 0; i < M; i ++) {
        cin >> n;
        auto it = nums.upper_bound(n);
        if(it != nums.begin()) {
            cout << *prev(it) << endl;
            nums.erase(prev(it));
        } else {
            cout << -1 << endl;
        }
    }
}
