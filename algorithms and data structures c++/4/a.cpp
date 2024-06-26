#include <iostream>
#include <vector>

int main() {
    int n, m;
    std::cin >> n >> m;

    std::vector<std::vector<int>> table(n, std::vector<int>(m));
    std::vector<std::vector<int>> result(n, std::vector<int>(m, 500));

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            std::cin >> table[i][j];
        }
    }

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (table[i][j] == 1) {
                for (int x = 0; x < n; ++x) {
                    for (int y = 0; y < m; ++y) {
                        result[x][y] = std::min(result[x][y], abs(x - i) + abs(y - j));
                    }
                }
            }
        }
    }

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            std::cout << result[i][j] << " ";
        }
        std::cout << std::endl;
    }

    return 0;
}
