#include <iostream>
using namespace std;

int main() {
    int a;
    cin >> a;

    int s = 0;
    while (a != 0) {
        s += a;
        cin >> a;
    }

    cout << s;
}