#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <algorithm>

int firstUp(int num) {
    int firstDigit = num / 1000;
    if (firstDigit == 9) {
        return 0;
    }
    return num + 1000;
}

int lastDown(int num) {
    int lastDigit = num % 10;
    if (lastDigit == 1) {
        return 0;
    }
    return num - 1;
}

int shiftLeft(int num) {
    return (num % 1000) * 10 + num / 1000;
}

int shiftRight(int num) {
    return num / 10 + (num % 10) * 1000;
}

int main() {
    int startNum, endNum;
    std::cin >> startNum >> endNum;

    std::unordered_map<int, std::pair<int, int>> distPrev;
    distPrev[startNum] = {0, -1};

    std::queue<int> q;
    q.push(startNum);

    while (!q.empty()) {
        int currentNum = q.front();
        q.pop();

        int currentDist = distPrev[currentNum].first;

        std::vector<int> neighbors = {firstUp(currentNum), lastDown(currentNum), 
                                      shiftLeft(currentNum), shiftRight(currentNum)};
        for (int neighbor : neighbors) {
            if (neighbor != 0 && distPrev.count(neighbor) == 0) {
                distPrev[neighbor] = {currentDist + 1, currentNum};
                q.push(neighbor);
            }
        }

        if (distPrev.count(endNum) > 0) {
            break;
        }
    }

    if (distPrev.count(endNum) == 0) {
        std::cout << -1;
    } else {
        std::vector<int> path;
        int current = endNum;
        while (current != -1) {
            path.push_back(current);
            current = distPrev[current].second;
        }
        std::reverse(path.begin(), path.end());

        for (int num : path) {
            std::cout << num << '\n';
        }
    }

    return 0;
}
