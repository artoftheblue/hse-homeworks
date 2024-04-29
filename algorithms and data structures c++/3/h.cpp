#include <iostream>
#include <stack>
#include <vector>

void DFS(std::vector<std::vector<int>> &graph, std::vector<int>& colors, int vertex) {
    colors[vertex] = 1;

    for (auto& v : graph[vertex]) {
        if (colors[v] == -1) {
            DFS(graph, colors, v);
        }
    }
    colors[vertex] = 2;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int n;
    std::cin >> n;
    
    std::vector<std::vector<int>> graph(n + 1);
    std::vector<int> colors(n + 1, -1);
    
    std::vector<std::vector<int>> graph2(n + 1);
    std::vector<int> colors2(n + 1, -1);
    
    graph.resize(n + 1);
    colors.assign(n + 1, -1);

    for (int i = 1; i < n + 1; ++i) {
        for (int j = 1; j < n + 1; j++) {
            int a;
            std::cin >> a;
            if (a == 1) {
                graph[i].push_back(j);
                graph2[j].push_back(i);
            }
        }
    }
    
    DFS(graph2, colors, 1);
    DFS(graph, colors2, 1);

    for (int i = 1; i < n + 1; ++i) {
        if (colors[i] == -1 || colors2[i] == -1) {
            std::cout << "NO";
            return 0;
        }
    }

    std::cout << "YES";
    return 0;
}