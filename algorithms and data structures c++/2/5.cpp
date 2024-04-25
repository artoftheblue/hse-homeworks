#include <iostream>
#include <vector>

struct Edge {
    int to;
    int number;
};

int n;
std::vector<std::vector<Edge>> matrix;
std::vector<long long> frequencies;
std::vector<int> visited;
int global_counter;

void DFS_simple(int x) {
    visited[x] = 1;
    ++global_counter;
    for (auto& vertex : matrix[x]) {
        if (vertex.to != x && visited[vertex.to] != 1) {
            DFS_simple(vertex.to);
        }
    }
}

long long DFS(int x, int parent) {
    long long subtree_size = 1;
    for (auto& edge : matrix[x]) {
        if (edge.to != parent) {
            long long temp_value = DFS(edge.to, x);
            frequencies[edge.number] = temp_value * (global_counter - temp_value);
            
            subtree_size += temp_value; 
        }
    }
    return subtree_size;
}

int main() {
    int m;
    std::cin >> n >> m;
    matrix.resize(n);
    visited.assign(n, 0);
    frequencies.assign(m, 0);
    
    int counter = 0;
    for (int i = 0; i < m; ++i) {
        int a, b;
        std::cin >> a >> b;
        matrix[a - 1].push_back({b - 1, counter});  
        matrix[b - 1].push_back({a - 1, counter});
        ++counter;
    }
    
    for (int i = 0; i < n; ++i) {
        if (visited[i] == 0) {
            global_counter = 0;
            DFS_simple(i);
            DFS(i, -1); 
        }
    }
    
    int q;
    std::cin >> q;
    for (int i = 0; i < q; ++i) {
        int query;
        std::cin >> query;
        std::cout << frequencies[query - 1] << std::endl;
    }
    
    return 0;
}