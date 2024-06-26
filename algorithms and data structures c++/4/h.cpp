#include <iostream>
#include <vector>
#include <deque>

// код с семинара

const int inf = 1 << 20;

using namespace std;

int main() {
    std::ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    size_t n = 0, m = 0;
    cin >> n >> m;

    vector<int> color(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> color[i];
    }
    vector<vector<size_t>> gr(n + 1);

    for (int i = 0; i < m; ++i) {
        size_t u, v;
        cin >> u >> v;
        gr[v].push_back(u);
        gr[u].push_back(v);
    }

    vector<int> dist(n + 1, inf);
    vector<int> p(n + 1, -1);
    dist[1] = 0;
    deque<size_t> q;
    q.push_back(1);

    while (!q.empty()) {
        size_t cur = q.front();
        q.pop_front();
        for (const auto &to: gr[cur]) {
            int w = abs(color[to] - color[cur]);
            if (dist[to] > dist[cur] + w) {
                dist[to] = dist[cur] + w;
                p[to] = cur;
                if (w == 0) {
                    q.push_front(to);

                } else {
                    q.push_back(to);

                }

            }
        }

    }
    if (dist[n] != inf) {
        cout << dist[n] << ' ';
        vector<int> path;
        int v = n;
        while (v != -1) {
            path.push_back(v);
            v = p[v];
        }
        cout << path.size() << '\n';
        for (int i = path.size() - 1; i >= 0; --i) {
            cout << path[i] << ' ';
        }
    } else {
        cout << "impossible";
    }


    return 0;
}