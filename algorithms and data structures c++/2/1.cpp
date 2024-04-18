#include <iostream>
#include <vector>
#include <algorithm>

int n;
std::vector<std::vector<int>> matrix;
std::vector<int> distances;

void DFS(int x, int dist) {
    distances[x] = dist;
    for (auto& vertex : matrix[x]) {
        DFS(vertex, dist + 1);
    }
}

int main() {
    std::cin >> n;
    matrix.resize(n);
    distances.resize(n);
    
    for (int i = 1; i < n; ++i) {
        int a;
        std::cin >> a;
        matrix[a - 1].push_back(i);
    }
    
    DFS(0, 0);
    
    int max_dist = 0;
    for (auto& distance : distances) {
        if (distance > max_dist) {
            max_dist = distance;
        }
    }
    std::cout << max_dist << std::endl;
    
    int counter = 0;
    std::vector<int> numbers;
    for (int i = 0; i < n; ++i) {
        if (distances[i] == max_dist) {
            ++counter;
            numbers.push_back(i);
        }
    }
    
    std::cout << counter << std::endl;
    for (auto& number : numbers) {
        std::cout << number + 1 << " ";
    }
    return 0;
}