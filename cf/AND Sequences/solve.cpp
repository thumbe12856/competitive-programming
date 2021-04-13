#include <map>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
#include <limits.h>

using namespace std;

const long long MOD = 1e9 + 7;

long long solve(long long N, vector<long long>& A) {
    long long i, j, k;
    long long val = A[0];
    map<long long, long long> vis;
    vis[A[0]] += 1;
    for(i = 1; i < N; i++) {
        val &= A[i];
        vis[A[i]] += 1;
    }

    val = vis[val];
    if(val == 1) {
        return 0;
    }

    long long ans = val * (val - 1);
    for(i = 1; i < N - 1; i++) {
        ans = ans * i % MOD;
    }

    return ans;
}

int main() {
    long long T, N, K;
    int i, j, k;
    cin >> T;
    while(T--) {
        cin >> N;
        vector<long long> A(N);
        for(i = 0; i < N; i++) {
            cin >> A[i];
        }
        cout << solve(N, A) << endl;
    }

}
