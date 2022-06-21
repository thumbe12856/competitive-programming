#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <limits.h>

using namespace std;

long long ans;
long long dfs(
    map<int, vector<pair<int, int>>> & tree,
    int parent,
    int node) {

    long long res = 0;
    for (pair<int, int> p: tree[node]) {
        int next_node = p.first;
        int w = p.second;

        if (next_node == parent) {
            continue;
        }

        long long temp_res = w + dfs(tree, node, next_node);
        ans = max(ans, res + temp_res);
        res = max(res, temp_res);
    }

    return res;
}

void solve(map<int, vector<pair<int, int>>>& tree) {
    dfs(tree, 0, 1);
}

int main() {
    int f, t, w;
    // tree[node] = [
    //     (next_node1, w1), (next_node2, w2), ...
    // ]
    map<int, vector<pair<int, int>>> tree;
	while (cin >> f >> t >> w) {
        tree[f].push_back({t, w});
        tree[t].push_back({f, w});
	}

    ans = 0;
    solve(tree);
    cout << ans << endl;

	return 0;
}
