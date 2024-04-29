#include <iostream>
#include <stack>
#include <vector>

std::vector<std::vector<int>> graph;
std::vector<int> colors;

void DFS(int vertex) {
    colors[vertex] = 1;

    for (auto& v : graph[vertex]) {
        if (colors[v] == 1) {
            std::cout << 1;
            exit(0);
        }
        DFS(v);
    }

    colors[vertex] = 2;
}



int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int n;
    std::cin >> n;

    graph.resize(n + 1);
    colors.assign(n + 1, -1);

    for (int i = 1; i < n + 1; ++i) {
        for (int j = 1; j < n + 1; j++) {
            int a;
            std::cin >> a;
            if (a == 1) {
                graph[i].push_back(j);
            }
        }
    }

    for (int i = 1; i < n + 1; ++i) {
        if (colors[i] == -1) {
            DFS(i);
        }
    }

    std::cout << 0;
    return 0;
}