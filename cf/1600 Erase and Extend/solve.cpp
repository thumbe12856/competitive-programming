#pragma GCC optimize("Ofast,no-stack-protector")

#include <bits/stdc++.h>
#include <limits.h>

#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <vector>

using namespace std;

std::set<string> vis;
std::set<int> can;
vector<vector<int>> G(200001);
vector<vector<std::pair<int, int>>> q(200001);
vector<pair<int, int>> dirs;
string ans = "";

void dfs(string curr, int K) {
    if (vis.find(curr) != vis.end() || curr.size() == 0) {
        return;
    }
    vis.insert(curr);
    // cout << vis.size() << endl;
    // cout << curr << endl;

    if (curr.size() == K) {
        if (ans == "") {
            ans = curr;
        } else {
            ans = min(ans, curr);
        }
    } else if (curr.size() > K) {
        dfs(curr.substr(0, K), K);
        return;
    }

    string tmp = curr;
    tmp.pop_back();
    dfs(tmp, K);
    dfs(curr + curr, K);
}

void bruteForce(string &s, int N, int K) {
    vis.clear();
    ans = "";
    dfs(s, K);
}

string solve(string &s, int N, int K) {
    s += s;
    string curr = "";
    curr += s[0];
    string target = "";

    for (int i = 1; i < N; i++) {
        if (s.substr(i, curr.size()) > curr) {
            break;
        } else {
            curr += s[i];
        }
    }

    while (curr.size() < K) {
        curr += curr;
    }
    return curr.substr(0, K);
}

int main() {
    int T, N, K;
    string s;
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N >> K;
    cin >> s;
    string ans_s = solve(s, N, K);
    cout << ans_s << endl;
    return 0;
}
