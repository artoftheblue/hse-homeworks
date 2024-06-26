#include <iostream>
#include <vector>
#include <queue>
#include <climits>

int main() {
    int n, m;
    std::cin >> n >> m;

    std::vector<std::vector<char>> matrix(n, std::vector<char>(m));
    std::vector<std::vector<int>> distances(n, std::vector<int>(m, INT_MAX));
    distances[0][0] = 0;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            std::cin >> matrix[i][j];
        }
    }

    int min_distance = INT_MAX;
    std::queue<std::pair<std::pair<int, int>, std::pair<int, int>>> q;
    q.push(std::pair<std::pair<int, int>, std::pair<int, int>>(std::pair<int, int>(0, 0), std::pair<int, int>(0, 0)));

    std::vector<std::pair<int, int>> differences {std::pair<int, int>(-1, 0), std::pair<int, int>(1, 0), std::pair<int, int>(0, -1), std::pair<int, int>(0, 1)};

    while (!q.empty()) {
        std::pair<std::pair<int, int>, std::pair<int, int>> current = q.front();
        std::pair<int, int> now = current.first;
        std::pair<int, int> prev_distance = current.second;
        q.pop();
        int y = now.first;
        int x = now.second;

        for (const auto& diff : differences) {
            if (!(prev_distance.first + diff.first == 0 && prev_distance.second + diff.second == 0)) {
                std::pair<int, int> next = now;
                while (0 <= next.first + diff.first && next.first + diff.first < n &&
                       0 <= next.second + diff.second && next.second + diff.second < m) {
                    if (matrix[next.first + diff.first][next.second + diff.second] == '0') {
                        next = std::pair<int, int>(next.first + diff.first, next.second + diff.second);
                    } else if (matrix[next.first + diff.first][next.second + diff.second] == '2') {
                        next = std::pair<int, int>(next.first + diff.first, next.second + diff.second);
                        break;
                    } else {
                        break;
                    }
                }
    
                if (distances[next.first][next.second] > distances[now.first][now.second] + 1) {
                    distances[next.first][next.second] = distances[now.first][now.second] + 1;
                    q.push(std::pair<std::pair<int, int>, std::pair<int, int>>(next, diff));
                }
    
                if (matrix[next.first][next.second] == '2') {
                    min_distance = std::min(min_distance, distances[next.first][next.second]);
                }
            }
        }
    }

    std::cout << min_distance << std::endl;

    return 0;
}