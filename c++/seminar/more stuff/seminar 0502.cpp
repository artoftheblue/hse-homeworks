#include<iostream>
#include<vector>
 
template<typename T>
class Vector {
    T* arr;
    size_t sz = 0;
    size_t cap = 0;
public:
    Vector() = default;
 
    Vector(size_t sz) : sz(sz) {
        arr = new T[sz];
    }
 
    void push_back(T value) {
        if (sz == 0) {
            cap = 1;
            arr = new T[1];
        } else if (sz == cap) {
            cap *= 2;
            T* tmp = new T[cap];
            for (size_t i = 0; i < sz; ++i){
                tmp[i] = arr[i];
            }
            delete[] arr;
            arr = tmp;
 
        }
        arr[sz] = value;
        ++sz;
    }
    
    T back() {
        return arr[sz];
    }
    
    T pop_back() {
        --sz;
        T temp = arr[sz];
        if (cap > 2 * sz) {
            cap /= 2;
        }
        return temp;
    }
 
    size_t size() {
        return sz;
    }
 
    size_t capacity() {
        return cap;
    }
 
    ~Vector() {
        delete[] arr;
    }
};
 
 
int main() {
    Vector<int> v;
    for (int i = 0; i < 5; ++i) {
        v.push_back(i);
        std::cout << v.size() << ' ' << v.capacity() << '\n';
    }

    for (int i = 0; i < 5; ++i) {
        std::cout << v.pop_back() << ' ' << v.size() << ' ' << v.capacity()<< '\n';
    }
    return 0;
}