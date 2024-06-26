#include <iostream>
#include <vector>
#include <limits>
#include <queue>
#include <algorithm>

const int INF = 2009000999; 

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int NUM;
    std::cin >> NUM;

    for (int graphNum = 0; graphNum < NUM; ++graphNum) {
        int N, M;
        std::cin >> N >> M;

        std::vector<std::vector<std::pair<int, int>>> graph(N);
        for (int i = 0; i < M; ++i) {
            int u, v, weight;
            std::cin >> u >> v >> weight;
            graph[u].emplace_back(v, weight);
            graph[v].emplace_back(u, weight);
        }

        int startNode;
        std::cin >> startNode;

        std::vector<int> dist(N, INF);
        dist[startNode] = 0;

        std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, std::greater<std::pair<int, int>>> pq;
        pq.push({0, startNode});

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

        for (int i = 0; i < N; ++i) {
            std::cout << dist[i] << ' ';
        }
        std::cout << std::endl;
    }

    return 0;
}