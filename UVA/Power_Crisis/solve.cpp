#include <vector>
#include <iostream>
#include <climits>
#include <math.h>
#include <string>
#include <vector>
#include <set>

using namespace std;

bool solve(int N, int M) {
    vector<int> nums(N + 1);
    nums[1] = 1;
    int cnt = N - 2;
    int idx = 1;
    while (cnt) {
        int k = M;
        while (true) {
            if (idx > N) {
                idx -= N;
            }

            if (nums[idx] == 0) {
                k -= 1;
                if (k == 0) {
                    nums[idx] = 1;
                    break;
                }
            }

            idx += 1;
        }

        cnt -= 1;
    }

    if (nums[13] == 0) {
        return true;
    }
    return false;
}

int main() {
    int N;
    while (cin >> N) {
        if (N == 0) {
            break;
        }

        for (int M = 1;; M ++) {
            if (solve(N, M)) {
                cout << M << endl;
                break;
            }
        }
    }

    return 0;
}
