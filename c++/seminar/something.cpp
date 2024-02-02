#include <iostream>
#include <vector>

template<typename T>
struct Point {
    T x = 0;
    T y = 0;
    Point(T x, T y): x(x), y(y){};

    Point() = default;

    Point operator+ (const Point &other) const {
        return Point<T>(this->x + other.x, this->y + other.y);
    }

    Point operator- (const Point &other) const {
        return Point<T>(this->x - other.x, this->y - other.y);
    }

    friend std::ostream& operator << (std::ostream &os, const Point& p) {
        os << p.x << ' ' << p.y;
        return os;
    }

    friend std::istream& operator >> (std::istream &is, Point& p) {
        is >> p.x >> p.y;
        return is;
    }
};

int main() {
    Point<int> p1, p2;
    std::cin >> p1 >> p2;
    std::cout << p1 - p2;

    return 0;
}