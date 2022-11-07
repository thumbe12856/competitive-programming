#pragma GCC optimize("Ofast,no-stack-protector")

#include <bits/stdc++.h>
#include <limits.h>

#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <vector>

using namespace std;

bool dfs(long long root, set<long long> &seq, vector<long long> &curr) {
    if (curr.size() == seq.size()) {
        return true;
    }
    long long target = root * 3;
    if (seq.find(target) != seq.end()) {
        curr.push_back(target);
        if (dfs(target, seq, curr)) {
            return true;
        }
    }
    target = root / 2;
    if ((root & 1) == 0 && seq.find(target) != seq.end()) {
        curr.push_back(target);
        return dfs(target, seq, curr);
    }
    return false;
}

void solve(set<long long> &seq) {
    for (auto s : seq) {
        vector<long long> curr;
        curr.push_back(s);
        if (dfs(s, seq, curr)) {
            for (long long j = curr.size() - 1; j > -1; j--) {
                cout << curr[j] << " ";
            }
            cout << endl;
            break;
        }
    }
}

int main() {
    long long T, tmp;
    set<long long> seq;
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> T;
    for (long long i = 0; i < T; i++) {
        cin >> tmp;
        seq.insert(tmp);
    }
    solve(seq);
    return 0;
}
