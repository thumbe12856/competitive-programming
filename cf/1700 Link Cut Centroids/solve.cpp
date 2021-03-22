#include <map>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> G[100001];

int dfs(int N, int node, int parent, vector<int>& can, int& min_total) {

    int total = 1; // total children of the node.
    int res = 0; // total nodes connected of the node, children or N - children.

    for (int i = 0; i < G[node].size(); i++) {
        int next_node = G[node][i];
        if(next_node == parent) {
            continue;
        }

        int ret = dfs(N, next_node, node, can, min_total);
        total += ret;
        res = max(ret, res);
    }

    res = max(res, N - total);

    if(res < min_total) {
        min_total = res;
        can.clear();
        can.push_back(node);
    } else if(res == min_total) {
        can.push_back(node);
    }

    return total;
}

void solve(int N) {

    vector<int> can;
    int min_total = N;
    dfs(N, 1, 0, can, min_total);

    if(can.size() == 1) {
        cout << 1 << " " << G[1][0] << endl;
        cout << 1 << " " << G[1][0] << endl;
    } else {
        int v1 = can[0];
        int v2 = can[1];
        int target = -1;

        for(int i = 0; i < G[v1].size(); i++) {
            if(G[v1][i] != v2) {
                target = G[v1][i];
                break;
            }
        }

        cout << v1 << " " << target << endl;
        cout << v2 << " " << target << endl;
    }
}

int main(){
	int T, N, f, t;
    cin >> T;
    while(T--) {
        cin >> N;
        for(int i = 0; i <= N; i++) {
            G[i].clear();
        }

        int temp = N - 1;
        while(temp--) {
            cin >> f >> t;
            G[f].push_back(t);
            G[t].push_back(f);
        }

        solve(N);
	}
}
