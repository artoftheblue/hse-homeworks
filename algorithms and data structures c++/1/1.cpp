#include <iostream>
#include <vector>

int DFS(int x, int y, int n, std::vector<std::vector<int>>& int_matrix, std::vector<std::vector<char>>& char_matrix, int& counter) {
    // std::cout << x << y << std::endl;
    if (char_matrix[x][y] == '*' || int_matrix[x][y] == 1)
        return 1;
    ++counter;
    int_matrix[x][y] = 1;
    
    if (x + 1 < n)
        DFS(x + 1, y, n, int_matrix, char_matrix, counter);
    if (y + 1 < n)
        DFS(x, y + 1, n, int_matrix, char_matrix, counter);
    if (x - 1 > -1)
        DFS(x - 1, y, n, int_matrix, char_matrix, counter);
    if (y - 1 > -1)
        DFS(x, y - 1, n, int_matrix, char_matrix, counter);
    
    return 0;
}

int main() {
    int n;
    std::cin >> n;
    
    int counter = 0;
    
    std::vector<std::vector<int>> matrix(n, std::vector<int>(n));
    std::vector<std::vector<char>> char_matrix(n, std::vector<char>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            std::cin >> char_matrix[i][j];   
            matrix[i][j] = 0;
        }
    }
    
    int x, y;
    std::cin >> x >> y;
    
    DFS(x - 1, y - 1, n, matrix, char_matrix, counter);
    
    std::cout << counter << std::endl;
}
