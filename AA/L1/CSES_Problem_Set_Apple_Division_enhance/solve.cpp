#include <map>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
#include <limits.h>
#include <bits/stdc++.h>
#include <stdio.h>

using namespace std;

int nums[30];
long long N, s, l, r;

int get_bit(int mask, int pos) {
    return (mask >> pos) & 1;
}

int main() {
    cin >> N;
    for(int i = 0; i < N; i ++) {
        cin >> nums[i];
        s += nums[i];
    }

    long long ans = s;
    long long curr = 0;
    for(int i = 1; i < (1 << N); i++) {
        for(int j = 0; j < N; j++) {
            if(get_bit(i, j)) {
                curr += nums[j];
                break;
            } else {
                curr -= nums[j];
            }
        }

        ans = min(ans, abs(s - 2 * curr));
    }

    cout << ans << endl;
    return 0;
}
