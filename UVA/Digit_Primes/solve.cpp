#include <vector>
#include <iostream>
#include <climits>
#include <math.h>
#include <string>
#include <vector>
#include <set>

using namespace std;

int T, t1, t2;
vector<int> q;
set<int> all_primes;

bool check(int n) {
    int s = 0;
    while (n) {
        s += n % 10;
        n /= 10;
    }

    return all_primes.find(s) != all_primes.end();
}

int solve(int target) {
    int l = 0, r = q.size();
    while (l < r) {
        int mid = (r - l) / 2 + l;
        if (q[mid] <= target) {
            l = mid + 1;
        } else {
            r = mid;
        }
    }

    return l;
}

int main() {
    int limit = 1000000;
    vector<int> candidates(limit, 1);
    for (int i = 2; i <= limit; i ++) {
        if (candidates[i]) {
            for (int j = i; j <= limit; j += i) {
                candidates[j] = 0;
            }

            all_primes.insert(i);
        }
    }

    for (auto n: all_primes) {
        if (check(n)) {
            q.push_back(n);
        }
    }

    cin >> T;
    while (T--) {
        cin >> t1 >> t2;
        cout << solve(t2) - solve(t1 - 1) << endl;
    }

    return 0;
}
