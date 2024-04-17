#include <iostream>
#include <vector>

int DFS(int x, int n, std::vector<std::vector<int>>& matrix, std::vector<int>& visited) {
    if (visited[x] == 1) {
        return 0;
    }
    visited[x] = 1;
    
    for (int i = 0; i < n; ++i) {
        if (matrix[x][i] == 1 && visited[i] == 0) {
            DFS(i, n, matrix, visited);
        }
    }
    return 0;
}

int main() {
    int n, m;
    std::cin >> n >> m;
    
    int counter = 0;
    
    std::vector<std::vector<int>> matrix(n, std::vector<int>(n));
    std::vector<int> visited(n, 0);
    
    for (int i = 0; i < m; ++i) {
        int a, b;
        std::cin >> a >> b;
        matrix[a - 1][b - 1] = 1;
        matrix[b - 1][a - 1] = 1;
    }
    
    DFS(0, n, matrix, visited);
    
    for (int i = 0; i < n; ++i) {
        if (visited[i] == 0) {
            std::cout << "NO";
            return 0;
        }
    }
    std::cout << "YES";
    return 0;
}
