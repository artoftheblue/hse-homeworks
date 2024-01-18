#include <iostream>
using namespace std;

int main() {
    int a;
    cin >> a;

    if (a == 0) {
        cout << 0;
        return 0;
    }

    float s = 0;
    int c = 1;
    while (a != 0) {
        s += a;
        c += 1;
        cin >> a;
    }

    float result = (float) s / c;
    cout << fixed << result << endl;
}