#include<iostream>
#include<vector>
#include<math.h>
#include<string>

using namespace std;


void solve(int N) {
    int target = pow(10, N);
    int half = pow(10, N / 2);

    for (int i = 0; i < target; i ++) {
        int r = i % half;
        int l = i / half;

        if ((r + l) * (r + l) == i) {
            int j = i;
            int cnt = 0;
            while (j) {
                j /= 10;
                cnt ++;
            }

            if (i == 0) {
                cnt = 1;
            }

            for (int j = 0; j < N - cnt; j ++) {
                cout << "0";
            }
            cout << i << endl;
        }
    }
}

int main() {

    int N;
    while (cin >> N) {
        solve(N);
    }

    return 0;
}
