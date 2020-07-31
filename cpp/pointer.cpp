#include <iostream>
using namespace std;

int main() {
    int *p, i=2;
    p = &i;
    cout << p << " " << *p << endl;
    *p = 88;
    cout << p << " " << *p << endl;
    cout << &i << endl;

    // reference
    int & rei = i;
    cout << rei << " " << i << endl;
    cout << &rei << " " << endl;
    rei = 66;
    cout << rei << " " << i << endl;
    cout << &rei << " " << endl;
}