#include <iostream>
#include <stack>
#include <vector>

int n;

void DFS(std::vector<std::vector<int>>& graph, std::vector<int>& distances, int vertex, int parent) {
    distances[vertex] = distances[parent] + 1;

    for (auto& v : graph[vertex]) {
        if (v != parent) {
            DFS(graph, distances, v, vertex);
        }
    }
}

void get_farthest_distance(std::vector<int>& distances, int& vertex, int& total_length) {
    int current_maximum_distance = -1;
    int farthest_vertex = 0;
    
    for (int v = 1; v < n + 1; ++v) {
        if (distances[farthest_vertex] < distances[v]) {
            farthest_vertex = v;
            current_maximum_distance = distances[v];
        }
    }
    
    vertex = farthest_vertex;
    total_length = current_maximum_distance;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int max_kilometers;
    std::cin >> n >> max_kilometers;
    
    std::vector<std::vector<int>> graph(n + 1);
    std::vector<int> distances(n + 1, -1);
    
    graph.resize(n + 1);
    distances.assign(n + 1, -1);

    for (int i = 1; i < n; ++i) {
        int a, b;
        std::cin >> a >> b;

        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    
    int begin, end, distance;
    
    DFS(graph, distances, 1, 0);
    get_farthest_distance(distances, begin, distance);
    
    for (int i = 0; i < n + 1; ++i) {
        distances[i] = -1;
    }
    
    DFS(graph, distances, begin, 0);
    get_farthest_distance(distances, end, distance);

    int answer = 0;
    if (distance >= max_kilometers) {
        answer += max_kilometers + 1;
    } else {
        answer += distance + (max_kilometers - distance) / 2 + 1;
    }
    
    if (answer <= n) {
        std::cout << answer;
        return 0;
    }
    
    std::cout << n;
    return 0;
}