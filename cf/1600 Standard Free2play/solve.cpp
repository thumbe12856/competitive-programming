#include <map>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
#include <limits.h>

using namespace std;

vector<long> P(200001);

long long solve(long long N) {
    if(N == 1) {
        return 0;
    }

    long long ans = 0;
    long long idx = 0;
    long long next_h = P[1] + 1;
    while(idx < N - 2) {
        auto h = P[idx + 1] + 1;
        auto diff = h - P[idx + 2];
        if(diff > 2) {
            next_h = P[idx + 2] + 1;
            ans += 1;
            idx += 1;
        } else {
            next_h = P[idx + 2];
            idx += 2;
        }
    }

    if(next_h > P[N - 1] && P[N - 1] + 1 >= 3) {
        ans += 1;
    }

    return ans;
}

int main() {
    long long T, H, N;
    long long i, j, k;

    cin >> T;
    while(T--) {
        cin >> H >> N;
        for(i = 0; i < N; i++) {
            cin >> P[i];
        }
        cout << solve(N) << endl;
    }

    return 0;
}
