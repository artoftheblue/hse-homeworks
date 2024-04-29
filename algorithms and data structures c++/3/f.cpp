#include <iostream>
#include <stack>
#include <vector>

std::vector<std::vector<int>> graph;
std::vector<int> colors;
std::stack<int> stack;

void DFS(int vertex) {
    colors[vertex] = 1;

    for (auto& v : graph[vertex]) {
        if (colors[v] == 1) {
            std::cout << -1;
            exit(0);
        }
        if (colors[v] == -1) {
            DFS(v);
        } 
    }

    stack.push(vertex);
    colors[vertex] = 2;
}



int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int n, m;
    std::cin >> n >> m;

    graph.resize(n + 1);
    colors.assign(n + 1, -1);

    for (int i = 1; i < m + 1; ++i) {
        int a, b;
        std::cin >> a >> b;

        graph[a].push_back(b);
    }

    for (int i = 1; i < n + 1; ++i) {
        if (colors[i] == -1) {
            DFS(i);
        }
    }

    while (stack.size() > 0) {
        std::cout << stack.top() << ' ';
        stack.pop();
    }
    
    return 0;
}