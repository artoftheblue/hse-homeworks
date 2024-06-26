#include <iostream>
#include <vector>
#include <queue>

int main() {
    int K, N, j, i, m, s;
    std::cin >> K >> N >> j >> i >> m >> s;

    std::vector<std::vector<int>> visited(K, std::vector<int>(N, 0));
    std::vector<std::pair<int, int>> directions = {{-2, -1}, {-2, 1}, {2, -1}, {2, 1}, {-1, -2}, {-1, 2}, {1, -2}, {1, 2}};

    --j;
    --i;
    --m;
    --s;

    std::queue<std::pair<int, int>> q;
    q.push({j, i});
    visited[j][i] = 1;

    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        if (x == m && y == s) {
            std::cout << "YES" << std::endl;
            return 0;
        }

        for (const auto& dir : directions) {
            int new_x = x + dir.first;
            int new_y = y + dir.second;

            if (new_x >= 0 && new_x < K && new_y >= 0 && new_y < N && visited[new_x][new_y] == 0) {
                q.push({new_x, new_y});
                visited[new_x][new_y] = 1;
            }
        }
    }

    std::cout << "NO" << std::endl;

    return 0;
}