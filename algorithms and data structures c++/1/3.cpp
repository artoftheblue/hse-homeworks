#include <iostream>
#include <vector>

void DFS(int x, std::vector<std::vector<int>>& adj_list, std::vector<int>& visited, int& counter) {
    if (visited[x] != 0) {
        return;
    }
    
    visited[x] = counter;
    
    for (int i = 0; i < adj_list[x].size(); ++i) {
        int next = adj_list[x][i];
        if (visited[next] == 0) {
            DFS(next, adj_list, visited, counter);
        }
    }
}

int main() {
    int n, m;
    std::cin >> n >> m;
    
    std::vector<std::vector<int>> adj_list(n);
    std::vector<int> visited(n, 0);
    
    for (int i = 0; i < m; ++i) {
        int a, b;
        std::cin >> a >> b;
        adj_list[a - 1].push_back(b - 1);
        adj_list[b - 1].push_back(a - 1);
    }
    
    int counter = 1;
    
    for (int i = 0; i < n; ++i) {
        if (visited[i] == 0) {
            DFS(i, adj_list, visited, counter);
            ++counter;
        }
    }
    
    std::cout << counter - 1 << std::endl;
    
    for (int i = 0; i < n; ++i) {
        std::cout << visited[i] << " ";
    }
    std::cout << std::endl;
    
    return 0;
}