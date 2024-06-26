#include <iostream>
#include <vector>
#include <limits>
#include <queue>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N, S, F;
    std::cin >> N >> S >> F;

    std::vector<std::vector<std::pair<int, int>>> graph(N);
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            int weight;
            std::cin >> weight;
            if (weight != -1) {
                graph[i].emplace_back(j, weight);
            }
        }
    }

    const int INF = std::numeric_limits<int>::max();
    std::vector<int> dist(N, INF);
    dist[S - 1] = 0;

    std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, std::greater<std::pair<int, int>>> pq;
    pq.push({0, S - 1});

    while (!pq.empty()) {
        int u = pq.top().second;
        int d = pq.top().first;
        pq.pop();

        if (d > dist[u]) {
            continue;
        }

        for (const auto& edge : graph[u]) {
            int v = edge.first;
            int w = edge.second;

            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            }
        }
    }

    if (dist[F - 1] == INF) {
        std::cout << -1 << '\n';
    } else {
        std::cout << dist[F - 1] << '\n';
    }

    return 0;
}
