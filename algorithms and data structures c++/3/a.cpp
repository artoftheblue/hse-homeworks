#include <iostream>
#include <vector>
#include <algorithm>

int n;
std::vector<std::vector<int>> matrix;
std::vector<int> visited;
std::vector<int> distances;
int max_length;

void DFS(int x) {
    visited[x] = 1;

    for (auto& vertex : matrix[x]) {
        if (visited[vertex] == 0) {
            distances[vertex] = distances[x] + 1;
            DFS(vertex);
        }
    }
}

int get_max() {
    int max_dist = 0;
    int max_index = 0;
    for (int i = 0; i < n; ++i) {
        if (distances[i] > max_dist) {
            max_dist = distances[i];
            max_index = i;
        }
    }
    max_length = max_dist;
    return max_index;
}

int main() {
    std::cin >> n;
    matrix.resize(n);
    visited.assign(n, 0);
    distances.assign(n, 0);
    
    for (int i = 0; i < n - 1; ++i) {
        int a, b;
        std::cin >> a >> b;
        matrix[a - 1].push_back(b - 1);
        matrix[b - 1].push_back(a - 1);
    }
    
    distances[0] = 1;
    DFS(0);
    
    int next = get_max();
    distances.assign(n, 0);
    visited.assign(n, 0);
    
    distances[next] = 1;
    DFS(next);
    
    get_max();
    std::cout << max_length;
    return 0;
}