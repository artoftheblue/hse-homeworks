#include <iostream>
#include <vector>
using namespace std;

void multiply(vector<int>& num, int factor) {
    int carry = 0;
    for (int i = 0; i < num.size(); i++) {
        int prod = num[i] * factor + carry;
        num[i] = prod % 10;
        carry = prod / 10;
    }
    while (carry > 0) {
        num.push_back(carry % 10);
        carry /= 10;
    }
}

void print(vector<int>& num) {
    for (int i = num.size() - 1; i >= 0; i--) {
        cout << num[i];
    }
    cout << endl;
}

int main() {
    int n;
    cin >> n;
    vector<int> num = {1};
    for (int i = 0; i < n; i++) {
        multiply(num, 2);
    }
    print(num);
    return 0;
}