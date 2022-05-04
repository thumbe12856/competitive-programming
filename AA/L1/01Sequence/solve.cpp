#pragma GCC optimize("Ofast,no-stack-protector")

#include <map>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
#include <limits.h>
#include <bits/stdc++.h>

using namespace std;

long long int ans;
long long int sum;
int N, M, L, R, X;
priority_queue<int, vector<int>, greater<int>> q;

// void solve() {
//     ans = 0;
//     while(q.size() > 1) {
//         int a = q.top();
//         q.pop();
//         int b = q.top();
//         q.pop();

//         ans += a + b;
//         q.push(a + b);
//     }

//     cout << ans << endl;
// }

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);

    cin >> N >> M;
    for(int i = 0; i < M; i ++) {
        cin >> L >> R >> X;
    }

    

}
