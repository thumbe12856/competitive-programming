#include <iostream>
#include <string>
#include <vector>
#include <limits.h>

using namespace std;

string S1;
string S2;

int solve() {
	int M = S1.size();
	int N = S2.size();
	vector<vector<int>> dp(M + 1, vector<int> (N + 1, 0));

	for (int i = 0; i < M; i ++) {
		for (int j = 0; j < N; j ++) {
			if (S1[i] == S2[j]) {
				dp[i + 1][j + 1] = 1 + dp[i][j];
			} else {
				dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1]);
			}
		}
	}

	return dp[M][N];
}

int main() {
	while (cin >> S1 >> S2) {
		cout << solve() << endl;
	}
	return 0;
}
