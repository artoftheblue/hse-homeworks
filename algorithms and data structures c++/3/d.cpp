#include <iostream>
#include <string>
#include <vector>

void DFS(std::vector<std::vector<int>>& graph, std::vector<int>& colors, int vertex, int parent, int color) {
    if (colors[vertex] == (color + 1) % 2) {
        std::cout << "NO";
        exit(0);
    } else if (colors[vertex] == -1) {
        colors[vertex] = color;
    } else {
        return;
    }

    for (auto& v : graph[vertex]) {
        if (v != parent) {
            DFS(graph, colors, v, vertex, (color + 1) % 2);
        }
    }
}


int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    int n, m;
    std::cin >> n >> m;

    std::vector<std::vector<int>> graph(n + 1);
    std::vector<int> colors(n + 1, -1);

    for (int i = 1; i < m + 1; ++i) {
        int a, b;
        std::cin >> a >> b;

        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    for (int i = 1; i < n + 1; ++i) {
        if (colors[i] == -1) {
            DFS(graph, colors, i, -1, 0);
        }
    }

    std::cout << "YES";
    return 0;


}