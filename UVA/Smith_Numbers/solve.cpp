#include <map>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
#include <limits.h>
#include <bits/stdc++.h>

using namespace std;

int digit_sum(int n) {
    int res = 0;
    while (n) {
        res += n % 10;
        n /= 10;
    }
    return res;
}

int main() {
    int limit = 1000000;
    vector<int> table(limit + 1);
    vector<int> primes(limit + 1);
    for (int i = 2; i <= limit; i ++) {
        if (table[i] == 1) {
            continue;
        }

        primes[i] = 1;
        for (int j = i; j <= limit; j += i) {
            table[j] = 1;
        }
    }

    int T, N;
    cin >> T;
    while (T--) {
        cin >> N;
        int smith_num = N + 1;

        while (true) {
            int n = smith_num;
            int curr_sum = 0;

            for (int i = 2; i < (int)sqrt(n) + 1; i ++) {
                if (primes[i]) {
                    while (n % i == 0) {
                        n /= i;
                        curr_sum += digit_sum(i);
                    }
                }

                if (n == 0) {
                    break;
                }
            }

            if (n > 1) {
                curr_sum += digit_sum(n);
            }

            if (n != smith_num && curr_sum == digit_sum(smith_num)) {
                break;
            }
            smith_num += 1;
        }

        cout << smith_num << endl;
    }

    return 0;
}
