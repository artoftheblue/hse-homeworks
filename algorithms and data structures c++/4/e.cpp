#include <iostream>
#include <vector>
#include <string>

int DFS(const std::vector<std::string>& graph, std::vector<std::vector<int>>& distance, const std::pair<int, int>& now, const std::pair<int, int>& prev) {
    static const std::vector<std::pair<int, int>> deltas {std::pair<int, int>(-1, 0), std::pair<int, int>(1, 0), std::pair<int, int>(0, -1), std::pair<int, int>(0, 1)};

    distance[now.first][now.second] = distance[prev.first][prev.second] + 1;

    int maxRes = 0;

    for (const auto& d : deltas) {
        std::pair<int, int> next = std::pair<int, int>(now.first + d.first, now.second + d.second);
        if (next.first >= 0 && next.first < graph.size() && next.second >= 0 && next.second < graph[0].size()) {
            if (next != prev && graph[next.first][next.second] == '.') {
                int res = DFS(graph, distance, next, now);
                maxRes = std::max(maxRes, res);
            }
        }
    }

    return maxRes;
}

void getFurthest(const std::vector<std::vector<int>>& distance, std::pair<int, int>& vertex, int& length) {
    length = -1;

    for (int i = 0; i < distance.size(); ++i) {
        for (int j = 0; j < distance[i].size(); ++j) {
            if (distance[i][j] > length) {
                vertex = std::pair<int, int>(i, j);
                length = distance[i][j];
            }
        }
    }
}

int main() {
    int n, m;
    std::cin >> n >> m;

    std::vector<std::string> matrix(m);
    std::vector<std::vector<int>> lengths(m, std::vector<int>(n, -1));

    int startX = -1, startY = -1;

    for (int i = 0; i < m; ++i) {
        std::cin >> matrix[i];
        if (startX == -1) {
            for (int j = 0; j < n; ++j) {
                if (matrix[i][j] == '.') {
                    startX = j;
                    startY = i;
                    break;
                }
            }
        }
    }

    DFS(matrix, lengths, std::pair<int, int>(startY, startX), std::pair<int, int>(0, 0));

    std::pair<int, int> bestVertex;
    int bestDistance;
    getFurthest(lengths, bestVertex, bestDistance);

    lengths.assign(m, std::vector<int>(n, -1));
    DFS(matrix, lengths, bestVertex, std::pair<int, int>(0, 0));
    getFurthest(lengths, bestVertex, bestDistance);

    std::cout << bestDistance;

    return 0;
}
