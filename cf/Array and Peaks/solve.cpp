#include <map>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
#include <limits.h>

using namespace std;

void solve(int N, int K) {
    if(!(0 <= K && K <= (N - 1) / 2)) {
        cout << -1 << endl;
        return;
    }

    int i, j, k;
    vector<int> ans(N);
    vector<int> can;

    for(i = 0; i < N; i++) {
        can.push_back(i + 1);
    }

    for(i = 0; i < K; i++) {
        ans[i * 2 + 1] = can.back();
        can.pop_back();
    }


    for(i = 0; i < N; i++) {
        if(ans[i] == 0) {
            ans[i] = can.back();
            can.pop_back();
        }
    }

    for(i = 0; i < N; i++) {
        cout << ans[i] << " ";
    }
    cout << endl;
}

int main() {
    int T, N, K;

    cin >> T;
    while(T--) {
        cin >> N >> K;
        solve(N, K);
    }

}
