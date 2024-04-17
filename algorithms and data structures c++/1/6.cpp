#include <iostream>
#include <vector>

std::vector<int> path;

int DFS(int x, int n, std::vector<std::vector<int>>& matrix, std::vector<int>& color) {
    color[x] = 1;
    
    for (auto& vertex : matrix[x]) {
        if (color[vertex] == 0) {
            path.push_back(vertex);
            if (DFS(vertex, n, matrix, color) == 1) {
                return 1;
            }
            path.pop_back();
        } else if (color[vertex] == 1) {
            path.push_back(vertex);
            return 1; 
        }
    }
    
    color[x] = 2;
    return 0;
}

void printPath() {
    int start = path.back();
                
    int size = path.size() - 2;
    int j = size;
    while (path[j] != start) {
        --j;
    }
    
    int k = j;
    while (k <= size) {
        ++k;
        std::cout << path[k] + 1 << " ";
    }
    std::cout << std::endl;
}

int main() {
    int n, m;
    std::cin >> n >> m;
    
    std::vector<std::vector<int>> matrix(n);
    std::vector<int> color(n, 0);
    
    for (int i = 0; i < m; ++i) {
        int a, b;
        std::cin >> a >> b;
        matrix[a - 1].push_back(b - 1);
    }
    
    int status = 0;
    for (int i = 0; i < n; ++i) {
        if (color[i] == 0) {
            path.push_back(i);
            if (DFS(i, n, matrix, color) == 1) {
                std::cout << "YES" << std::endl;
                printPath();
                return 0;
            }
        }
    }
    
    std::cout << "NO";
    return 0;
}