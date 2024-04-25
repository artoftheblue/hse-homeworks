#include <iostream>
#include <vector>
#include <algorithm>

int n, m, time_tracker;
std::vector<std::vector<int>> matrix;
std::vector<int> visited, entry_time, lowest_time;

int cute_points_counter;
std::vector<int> cute_points;

void DFS(int v, int parent) {
    visited[v] = 1;
    ++time_tracker;

    entry_time[v] = time_tracker;
    lowest_time[v] = time_tracker;
    
    int counter = 0;
    int saved = 0;
    for (auto& u : matrix[v]) {
        if (u == parent) {
            continue;
        } else if (visited[u] == 1) {
            lowest_time[v] = std::min(lowest_time[v], entry_time[u]);
        } else {
            DFS(u, v);
            lowest_time[v] = std::min(lowest_time[v], lowest_time[u]);
            ++counter;
            if (parent != -1 && lowest_time[u] >= entry_time[v] && cute_points[v] != 1) {
                ++cute_points_counter;
                cute_points[v] = 1;
            }
        }
    }
    
    if (parent == -1 && counter > 1 && cute_points[v] != 1) {
        ++cute_points_counter;
        cute_points[v] = 1;
    }
}

int main() {
    std::cin >> n >> m;
    matrix.resize(n);
    visited.assign(n, 0);
    entry_time.assign(n, -1);
    lowest_time.assign(n, -1);
    cute_points.assign(n, 0);
    cute_points_counter = 0;
    time_tracker = 0;

    for (int i = 0; i < m; ++i) {
        int a, b;
        std::cin >> a >> b;
        matrix[a - 1].push_back(b - 1);
        matrix[b - 1].push_back(a - 1);
    }

    for (int i = 0; i < n; ++i) {
        if (visited[i] == 0) {
            DFS(i, -1);
        }
    }

    std::cout << cute_points_counter << std::endl;

    for (int i = 0; i < n; ++i) {
        if (cute_points[i] == 1) {
            std::cout << i + 1 << std::endl;   
        }
    }
    return 0;
}