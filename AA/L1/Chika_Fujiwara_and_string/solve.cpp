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

    int N;
    cin >> N;

    set<string> vis;
    string S;
    for(int i = 0; i < N; i ++) {
        cin >> S;
        auto it = vis.upper_bound(S);
        if(it == vis.begin()) {
            cout << -1 << endl;
        } else {
            cout << *prev(it) << endl;
        }

        vis.insert(S);
    }

    return 0;
}
