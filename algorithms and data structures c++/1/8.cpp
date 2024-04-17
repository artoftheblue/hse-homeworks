#include <iostream>
#include <vector>

std::vector<std::vector<int>> children;
std::vector<int> visited;
std::vector<int> answers;
int n;

int get_independent_set(int u) {     
    if (answers[u] != -1) {
        return answers[u];
    }
    int children_sum = 0;
    int grandchildren_sum = 0;
    for (auto& child : children[u]) {
        children_sum += get_independent_set(child);
    }
    for (auto& child : children[u]) {
        for (auto& grandchild : children[child]) {
            grandchildren_sum += get_independent_set(grandchild);
        }
    }
    
    answers[u] = std::max(1 + grandchildren_sum, children_sum);
    return answers[u];
}

int main() {
    std::cin >> n;
    
    children.resize(n);
    visited.resize(n, 0);
    answers.resize(n, -1);
    
    int root;
    
    for (int i = 0; i < n; ++i) {
        int a;
        std::cin >> a;
        if (a != 0) {
            children[a - 1].push_back(i);
        } else {
            root = i;
        }
    }
    
    std::cout << get_independent_set(root);
    
    /*for (auto& item : answers) {
        std::cout << item << " ";
    }
    std::cout << std::endl;*/
}