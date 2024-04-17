#include <iostream>
#include <vector>

void DFS(int x, int n, std::vector<std::vector<int>>& matrix, std::vector<int>& visited, std::vector<int>& current, int& status) {
    visited[x] = 1;
    current[x] = 1;
    
    for (int i = 0; i < n; ++i) {
        if (matrix[x][i] == 1) {
            if (visited[i] == 0) {
                DFS(i, n, matrix, visited, current, status);
            } else if (current[i] == 1) {
                status = 1;
            }
        }
    }
    
    current[x] = 0;
}

int main() {
    int n;
    std::cin >> n;
    
    std::vector<std::vector<int>> matrix(n, std::vector<int>(n));
    std::vector<int> visited(n, 0);
    std::vector<int> current(n, 0);
    
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            std::cin >> matrix[i][j];
        }
    }
    
    int status = 0;
    for (int i = 0; i < n; ++i) {
        if (visited[i] == 0) {
            DFS(i, n, matrix, visited, current, status);
        }
    }
    
    std::cout << status;
    
    return 0;
}