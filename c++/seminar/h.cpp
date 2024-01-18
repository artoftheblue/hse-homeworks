#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    if (a + b <= c || a + c <= b || b + c <= a) {
        cout << "impossible" << endl;
    } else {
        if (a*a + b*b == c*c || a*a + c*c == b*b || b*b + c*c == a*a) {
            cout << "right" << endl;
        } else if (a*a + b*b > c*c && a*a + c*c > b*b && b*b + c*c > a*a) {
            cout << "acute" << endl;
        } else {
            cout << "obtuse" << endl;
        }
    }
    return 0;
}