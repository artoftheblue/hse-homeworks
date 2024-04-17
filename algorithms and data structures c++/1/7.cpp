#include <iostream>
#include <vector>

std::vector<std::vector<int>> matrix;
std::vector<int> visited;
std::vector<int> path;
int n;

void DFS(int x) {
    visited[x] = 1;
    path.push_back(x);
    
    for (int i = 0; i < n; ++i) {
        if (matrix[x][i] == 1 && i != x) {
            if (visited[i] == 0) {
                DFS(i);
                path.push_back(x);
            }
        }
    }
}

int main() {
    int m, v;
    std::cin >> n >> m >> v;
    
    matrix.resize(n, std::vector<int>(n));
    visited.assign(n, 0);
    
    for (int i = 0; i < m; ++i) {
        int a, b;
        std::cin >> a >> b;
        matrix[a - 1][b - 1] = 1;
        matrix[b - 1][a - 1] = 1;
    }
    
    DFS(v - 1);
    
    std::cout << path.size() << std::endl;
    for (auto& item : path) {
        std::cout << item + 1 << " ";
    }
    std::cout << std::endl;
}
