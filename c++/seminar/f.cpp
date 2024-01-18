#include <iostream>
using namespace std;

int main() {
    int a, b, n;
    cin >> a;
    cin >> b;
    cin >> n;
    int total = (a * 100 + b) * n;
    cout << total / 100 << " ";
    cout << total % 100 << endl;
    return 0;
}