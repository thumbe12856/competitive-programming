#include <map>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
#include <limits.h>
#include <bits/stdc++.h>

using namespace std;

int main() {
    string S;
    string rS;
    while (cin >> S) {
        string rS(S);
        reverse(rS.begin(), rS.end());

        // S =  amanaplanacanal
        // rS = lanacanalpanama
        int s_idx = 0, rs_idx = 0;
        int cnt = 0;
        while (s_idx < S.size()) {
            if (S[s_idx] == rS[rs_idx]) {
                s_idx += 1;
                rs_idx += 1;
                cnt += 1;
            } else {
                s_idx += 1;
                rs_idx = 0;
                cnt = 0;
            }
        }

        cout << S;
        for (int i = rs_idx; i < S.size(); i ++) {
            cout << rS[i];
        }
        cout << endl;
    }

    return 0;
}
