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

    int N, M, X, K, n;
    multiset<int> nums;

    cin >> N >> M >> X >> K;
    for(int i = 0; i < N; i ++) {
        cin >> n;
        nums.insert(n);
    }

    multiset<int> first_groups;
    multiset<int> second_groups;
    int i = 1;
    long long ans = 0;
    for(auto n : nums) {
        if(i < K) {
            first_groups.insert(n);
        } else if(K <= i && i <= K + X - 1) {
            second_groups.insert(n);
            ans += n;
        }

        i ++;
    }

    int fb = 0;
    int fe = 0;
    int sb = 0;
    int se = 0;
    cout << ans << endl;
    for(int i = 0; i < M; i ++) {
        cin >> n;

        if(first_groups.size() > 0) {
            fb = *next(first_groups.begin());
            fe = *prev(first_groups.end());
        }
        sb = *next(second_groups.begin());
        se = *prev(second_groups.end());

        if(fe <= n && n <= se) {
            ans += n;
            ans -= se;
            second_groups.insert(n);
            second_groups.erase(second_groups.find(se));
        } else if (n < fe) {
            first_groups.insert(n);
            first_groups.erase(first_groups.find(fe));

            ans += fe;
            ans -= se;
            second_groups.insert(fe);
            second_groups.erase(second_groups.find(se));
        }

        cout << ans << endl;
    }

    return 0;
}
