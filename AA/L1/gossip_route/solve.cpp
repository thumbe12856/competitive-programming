#include <map>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
#include <limits.h>
#include <bits/stdc++.h>

using namespace std;

std::set<int> vis;
std::set<int> can;
vector<int> nums(200010);
int N, Q, x, y;

void dfs(int node) {
    if(node == 1) {
        cout << 1;
        return;
    }

    dfs(nums[node]);
    cout << "->" << node;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);

    cin >> N;
    for(int i = 0; i < N - 1; i ++) {
        cin >> nums[i + 2];
    }
    nums[0] = 1;

    cin >> Q;
    for(int i = 0; i < Q; i ++) {
        cin >> x;
        dfs(x);
        cout << endl;
    }
}
