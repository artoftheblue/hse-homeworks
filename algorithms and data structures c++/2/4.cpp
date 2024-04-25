#include <iostream>
#include <vector>

int n;
std::vector<std::vector<int>> matrix(n);
std::vector<int> visited(n, 0);
std::vector<int> current(n, 0);

void DFS(int x) {
    visited[x] = 1;
    current[x] = 1;
    
    for (auto& edge : matrix[x]) {
        if (visited[edge] == 0) {
            DFS(edge);
        } else if (current[edge] == 1) {
            std::cout << "NO";
            exit(0);
        }
    }
    
    current[x] = 0;
}

int main() {
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(NULL);
    std::cin >> n;
    matrix.resize(n);
    visited.assign(n, 0);
    current.assign(n, 0);
    
    int out = 1;
    for (int i = 0; i < n - 1; ++i) {
        for (int j = out; j < n; ++j) {
            char color;
            std::cin >> color;
            if (color == 'B') {
                matrix[j].push_back(i);  
            } else if (color == 'R') {
                matrix[i].push_back(j);
            }
        }
        ++out;
    }
    
    for (int i = 0; i < n; ++i) {
        if (visited[i] == 0) {
            DFS(i);
        }
    }
    
    std::cout << "YES";
    return 0;
}


/*

#include <iostream>
#include <vector>
#include <algorithm>

int n;
std::vector<std::vector<int>> matrix_red;
std::vector<std::vector<int>> matrix_blue;
std::vector<int> reachable_red;
std::vector<int> reachable_blue;

void DFS(int vertex, std::vector<std::vector<int>>& matrix, std::vector<int>& reachable) {
    reachable[vertex] = 1;
    if (vertex != 0 && reachable_red[vertex] == 1 && reachable_blue[vertex] == 1) {
        std::cout << "NO";
        exit(0);
    }
    for (auto& edge : matrix[vertex]) {
        DFS(edge, matrix, reachable);
    }
}

int main() {
    std::cin >> n;
    matrix_red.resize(n);
    matrix_blue.resize(n);
    reachable_red.assign(n, 0);
    reachable_blue.assign(n, 0);
    
    int out = 1;
    for (int i = 0; i < n - 1; ++i) {
        for (int j = out; j < n; ++j) {
            char color;
            std::cin >> color;
            if (color == 'R') {
                matrix_red[i].push_back(j);  
            } else if (color == 'B') {
                matrix_blue[i].push_back(j);
            }
        }
        ++out;
    }
    
    /*for (auto& line : matrix) {
        for (auto& item : line) {
            std::cout << "(" << item.from << " " << item.to << " " << item.color << ") ";
        }
        std::cout << std::endl;
    }

    DFS(0, matrix_red, reachable_red);
    DFS(0, matrix_blue, reachable_blue);
    
    for (int i = 1; i < n; ++i) {
        if (reachable_red[i] == 1 && reachable_blue[i] == 1) {
            std::cout << "NO";
            return 0;
        }
        //std::cout << "(" << reachable_red[i] << ", " << reachable_blue[i] << ")\n";
    }
    
    std::cout << "YES";
    return 0;
}

#include <iostream>
#include <vector>
#include <algorithm>

struct Edge {
    char color; 
    int from;
    int to;
};

int n;
std::vector<std::vector<Edge>> matrix;
std::vector<int> only_red;
std::vector<int> only_blue;

void DFS(Edge& prev) {
    if (prev.from != -1) {
        if (prev.color == 'R') {
            if (only_blue[prev.from] == 1) {
                only_red[prev.to] = 0;
            } else {
                only_red[prev.to] = 1;
            }
        }
        if (prev.color == 'B') {
            if (only_red[prev.from] == 1) {
                only_blue[prev.to] = 0;
            } else {
                only_blue[prev.to] = 1;
            }
        } 
    }
    for (auto& edge : matrix[prev.to]) {
        DFS(edge);
    }
}

int main() {
    std::cin >> n;
    matrix.resize(n);
    only_red.assign(n, -1);
    only_blue.assign(n, -1);
    
    int out = 1;
    for (int i = 0; i < n - 1; ++i) {
        for (int j = out; j < n; ++j) {
            char color;
            std::cin >> color;
            matrix[i].push_back({color, i, j});            
        }
        ++out;
    }
    
    Edge start_edge = {'R', -1, 0};
    DFS(start_edge);
    
    for (int i = 0; i < n; ++i) {
        if (only_red[i] == 1 && only_blue[i] == 1) {
            std::cout << "NO";
            return 0;
        }
    }
    
    std::cout << "YES";
    return 0;
}

*/