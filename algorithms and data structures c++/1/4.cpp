#include <iostream>
#include <vector>

void DFS(int x, std::vector<std::vector<int>>& matrix, std::vector<int>& visited, int parent) {
    if (visited[x] == 1) {
        return;
    }
    
    visited[x] = 1;
    
    for (int i = 0; i < matrix[x].size(); ++i) {
        if (matrix[x][i] == 1) {
            if (visited[i] == 0) {
                DFS(i, matrix, visited, x);
            } else if (i != parent) {
                visited[i] = 2;
            }
        }
    }
}

int main() {
    int n, m;
    std::cin >> n >> m;
    
    std::vector<std::vector<int>> matrix(n, std::vector<int>(n));
    std::vector<int> visited(n, 0);
    
    for (int i = 0; i < m; ++i) {
        int a, b;
        std::cin >> a >> b;
        matrix[a - 1][b - 1] = 1;
        matrix[b - 1][a - 1] = 1;
    }
    
    DFS(0, matrix, visited, -1);
    
    for (int i = 0; i < n; ++i) {
        if (visited[i] != 1) {
            std::cout << "NO";
           return 0;
        }
    }
    
    std::cout << "YES";
    return 0;
}
