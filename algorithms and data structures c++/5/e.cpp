#include <iostream>
#include <vector>
#include <queue>
#include <limits>

const int INF = std::numeric_limits<int>::max();

struct Edge {
    int to;
    int time;
    int maxWeight;
};

int main() {
    int n, m;
    std::cin >> n >> m;

    std::vector<std::vector<Edge>> graph(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        int time, maxWeight;
        std::cin >> u >> v >> time >> maxWeight;
        graph[u].push_back({v, time, maxWeight});
        graph[v].push_back({u, time, maxWeight});
    }

    int startNode = 1;
    int endNode = n;

    int low = 0, high = 10000000;
    int maxMugs = 0;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        int currentWeight = 3000000 + mid * 100;

        std::vector<int> time(n + 1, INF);
        time[startNode] = 0;

        std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, std::greater<std::pair<int, int>>> pq;
        pq.push({0, startNode});

        while (!pq.empty()) {
            int u = pq.top().second;
            int currentTime = pq.top().first;
            pq.pop();

            if (currentTime > time[u]){
                continue;
            }

            for (const Edge& edge : graph[u]) {
                if (currentWeight <= edge.maxWeight && 
                    currentTime + edge.time < time[edge.to]) {
                    time[edge.to] = currentTime + edge.time;
                    pq.push({time[edge.to], edge.to});
                }
            }
        }

        if (time[endNode] <= 1440) {
            maxMugs = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    std::cout << maxMugs << std::endl;

    return 0;
}
