#include <map>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
#include <limits.h>

using namespace std;

int main() {
    int N;
    vector<int> A(3);
    vector<int> B(3);
    cin >> N;
    cin >> A[0] >> A[1] >> A[2];
    cin >> B[0] >> B[1] >> B[2];

    int a, b = INT_MAX;
    a = min(A[0], B[1]) + min(A[1], B[2]) + min(A[2], B[0]);

    vector<int> order = {0, 1, 2, 3, 4, 5};
    while(next_permutation(order.begin(), order.end())) {
        int val, res;
        vector<int> temp_A = A;
        vector<int> temp_B = B;
        for(auto idx : order) {
            switch(idx) {
                case 0:
                    val = min(temp_A[0], temp_B[0]);
                    temp_A[0] -= val;
                    temp_B[0] -= val;
                    break;

                case 1:
                    val = min(temp_A[1], temp_B[1]);
                    temp_A[1] -= val;
                    temp_B[1] -= val;
                    break;

                case 2:
                    val = min(temp_A[2], temp_B[2]);
                    temp_A[2] -= val;
                    temp_B[2] -= val;
                    break;

                case 3:
                    val = min(temp_B[0], temp_A[1]);
                    temp_A[1] -= val;
                    temp_B[0] -= val;
                    break;

                case 4:
                    val = min(temp_B[1], temp_A[2]);
                    temp_A[2] -= val;
                    temp_B[1] -= val;
                    break;

                case 5:
                    val = min(temp_B[2], temp_A[0]);
                    temp_A[0] -= val;
                    temp_B[2] -= val;
                    break;
            }
        }

        res = min(temp_A[0], temp_B[1]) + min(temp_A[1], temp_B[2]) + min(temp_A[2], temp_B[0]);
        b = min(res, b);
    }

    cout << b << " " << a << endl;
}
