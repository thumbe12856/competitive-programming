#pragma GCC optimize("Ofast,no-stack-protector")

#include <map>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
#include <limits.h>
#include <bits/stdc++.h>

using namespace std;

vector<long long int> A(200001);
vector<long long int> B(200001);
map<long long int, int> cnt_A;
map<long long int, int> vis_A;
map<long long int, int> cnt_B;
map<long long int, int> vis_B;
const long long int target = 1 << 20;
int vis[target];
int N;
long long int n;

template <typename Map>
bool map_compare (Map const &lhs, Map const &rhs) {
    // No predicate needed because there is operator== for pairs already.
    return lhs.size() == rhs.size()
        && std::equal(lhs.begin(), lhs.end(),
                      rhs.begin());
}

void cal(map<long long int, int>& cnt, long long int num) {
    while(!(num & 1)) {
        num >>= 1;
        cnt[2] += 1;
    }

    long long int k = 3;
    while(k <= num) {
        if(num % k == 0) {
            num /= k;
            cnt[k] += 1;
        } else {
            k += 2;
        }
    }
}

void solve() {
    for(long long int i = 2; i < target; i++) {
        if(vis[i] > 0) {
            continue;
        }
        for(long long int j = i; j < target; j += i) {
            vis[j] += 1;

            if(vis_A[j] > 0) {
                cnt_A[i] += vis_A[j];
            }

            if(vis_B[j] > 0) {
                cnt_B[i] += vis_B[j];
            }
        }
    }

    for(auto v: cnt_A) {
        cout << v.first << " " << v.second << endl;
    }

    for(auto v: cnt_B) {
        cout << v.first << " " << v.second << endl;
    }

    bool valid = true;
    if(!map_compare(cnt_A, cnt_B)) {
        valid = false;
    }

    if(valid) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }

}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);
    cin >> N;
    for(int i = 0; i < N; i ++) {
        cin >> n;
        vis_A[n] += 1;
    }
    for(int i = 0; i < N; i ++) {
        cin >> n;
        vis_B[n] += 1;
    }

    solve();
}
