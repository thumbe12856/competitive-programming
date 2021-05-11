#include <map>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
#include <limits.h>

using namespace std;

int dp[5001];
int presum[5001][5001];
int ori_presum[5001];

int main() {
    int N;
    int i, j, k, total, temp, x, y, last;
    int A[N];
    int B[N];

    cin >> N;
    for(i = 0; i < N; i++) {
        cin >> A[i];
    }
    for(i = 0; i < N; i++) {
        cin >> B[i];
    }

    total = 0;
    for(i = 0; i < N; i++) {
        for(j = 0; j < N; j++) {
            dp[j] = A[j] * B[i];

            if(i == j) {
                ori_presum[i] = total + dp[i];
                total += dp[i];
            }
        }

        for(j = 0; j < N; j++) {
            last = 0;
            if(i - 1 >= 0 && j + 1 < N) {
                last = presum[i - 1][j + 1];
            }
            presum[i][j] = last + dp[j];
        }
    }

    int ans = total;
    int lower, diff;
    for(i = 0; i < N; i++) {
        for(j = i + 1; j < N; j++) {
            temp = total;
            if(i - 1 >= 0) {
                lower = ori_presum[i - 1];
            } else {
                lower = 0;
            }

            temp -= ori_presum[j] - lower;

            diff = j - i + 1;
            if(j - diff >= 0 && i + diff < N) {
                lower = presum[j - diff][i + diff];
            } else {
                lower = 0;
            }

            temp += presum[j][i] - lower;
            if(temp > ans) {
                ans = temp;
            }

        }
    }

    cout << ans << endl;
    return 0;

}
