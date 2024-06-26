#include <iostream>
#include <vector>
#include <queue>
#include <unordered_set>

int main() {
    int N, M, v;
    std::cin >> N >> M >> v;

    std::vector<std::vector<int>> graph(N + 1);
    for (int i = 0; i < M; ++i) {
        int u, w;
        std::cin >> u >> w;
        graph[u].push_back(w);
        graph[w].push_back(u);
    }

    std::queue<int> q;
    std::unordered_set<int> visited;
    std::vector<int> order;

    q.push(v);
    visited.insert(v);

    while (!q.empty()) {
        int current = q.front();
        q.pop();
        order.push_back(current);

        for (int neighbor : graph[current]) {
            if (visited.find(neighbor) == visited.end()) {
                q.push(neighbor);
                visited.insert(neighbor);
            }
        }
    }

    std::cout << order.size() << std::endl;
    for (int vertex : order) {
        std::cout << vertex << " ";
    }
    std::cout << std::endl;

    return 0;
}
