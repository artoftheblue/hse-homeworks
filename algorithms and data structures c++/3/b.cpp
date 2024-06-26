#include <iostream>
#include <string>
#include <map>
#include <stack>
#include <deque>
#include <tuple>
#include <set>
#include <vector>
#include <algorithm>

std::vector<std::vector<int>> graph;
std::vector<int> colors;
std::vector<int> neighbours;

int DFS(int vertex, int parent) {
    if (graph[vertex][0] == parent and graph[vertex].size() == 1) {
        colors[vertex] = 0;
        return 0;
    }

    int maximum = -1;
    int center = -1;

    for (auto v : graph[vertex]) {
        if (v != parent) {
            center = DFS(v, vertex);
            maximum = std::max(center, maximum);
        }
    }

    colors[vertex] = maximum + 1;
    return maximum + 1;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int n;
    std::cin >> n;

    graph.resize(n + 1);
    colors.assign(n + 1, -2);
    neighbours.assign(n + 1, 0);

    for (int i = 1; i < n; ++i) {
        int a, b;
        std::cin >> a >> b;

        graph[a].push_back(b);
        ++neighbours[a];
        
        graph[b].push_back(a);
        ++neighbours[b];
    }

    if (n == 1) {
        std::cout << 0 << ' ' << 1 << ' ' << 1 << std::endl;
        exit(0);
    } 

    std::deque<std::pair<int, int>> children;

    for (int i = 1; i < n + 1; ++i){
        if (neighbours[i] == 1) {
            children.push_back({i, 0});
            colors[i] = -1;
        }
    }

    std::pair<int, int> me;
    
    while (!(children.empty())) {
        me = children.front();
        children.pop_front();

        colors[me.first] = me.second;

        for (auto& item : graph[me.first]) {
            neighbours[item] -= 1;
            if (neighbours[item] == 1) {
                children.push_back({item, me.second + 1});
                colors[item] = -1;
            }
        }
    }

    int saved_color = 0;
    std::vector<int> center_list;

    for (int i = 1; i < n + 1; ++i) {
        if (colors[i] == saved_color) {
            center_list.push_back(i);
        }
        if (colors[i] > saved_color) {
            center_list.clear();
            center_list.push_back(i);
            saved_color = colors[i];
        }
    }
    
    int size = center_list.size();

    colors.assign(n + 1, -1);

    int eccentricity = -1;
    eccentricity = DFS(center_list[0], -1);

    std::cout << eccentricity << ' ' << size << ' ';
    std::sort(center_list.begin(), center_list.end());

    for (int i = 0; i < size; ++i) {
        std::cout << center_list[i] << ' ';
    }
    std::cout << std::endl;

    return 0;

}