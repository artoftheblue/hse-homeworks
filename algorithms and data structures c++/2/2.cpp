#include <iostream>
#include <vector>
#include <algorithm>

struct Bridge {
    int number;
    int to;
};

int n, m, time_tracker;
std::vector<std::vector<Bridge>> matrix;
std::vector<int> visited, entry_time, lowest_time;

int bridge_counter;
std::vector<int> bridges;

void DFS(int x, int parent) {
    visited[x] = 1;
    ++time_tracker;

    entry_time[x] = time_tracker;
    lowest_time[x] = time_tracker;

    for (auto& vertex : matrix[x]) {
        if (vertex.to == parent) {
            continue;
        } else if (visited[vertex.to] == 1) {
            lowest_time[x] = std::min(lowest_time[x], entry_time[vertex.to]);
        } else {
            DFS(vertex.to, x);
            lowest_time[x] = std::min(lowest_time[x], lowest_time[vertex.to]);
            if (entry_time[x] < lowest_time[vertex.to]) {
                ++bridge_counter;
                bridges.push_back(vertex.number);
            }
        }
    }
}

int main() {
    std::cin >> n >> m;
    matrix.resize(n);
    visited.assign(n, 0);
    entry_time.assign(n, -1);
    lowest_time.assign(n, -1);

    for (int i = 0; i < m; ++i) {
        int a, b;
        std::cin >> a >> b;
        matrix[a - 1].push_back({i + 1, b - 1});
        matrix[b - 1].push_back({i + 1, a - 1});
    }

    for (int i = 0; i < n; ++i) {
        if (visited[i] == 0) {
            DFS(i, -1);
        }
    }

    std::sort(bridges.begin(), bridges.end());

    std::cout << bridge_counter << std::endl;

    for (auto& item : bridges) {
        std::cout << item << " ";
    }
    return 0;
}