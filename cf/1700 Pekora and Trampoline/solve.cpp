#include<bits/stdc++.h>
using namespace std;

long long int solve(int N, long long int* nums) {
    long long int ans = 0;

    for(int i = 0; i < N; i++) {
        long long int temp = 0;
        for(int j = 0; j < i; j++) {
            temp += max((long long int) 0, nums[j] - (i - j));
        }
        ans = max(ans, temp + nums[i] - 1);
    }

    return ans;
}

int main() {

    int T, N;
    cin >> T;
    while(T--) {
        cin >> N;
        long long nums[N];
        for(int i = 0; i < N; i++) {
            cin >> nums[i];
        }

        cout << solve(N, nums) << endl;
    }
    return 0;
}
