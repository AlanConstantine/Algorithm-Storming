#include <iostream>
using namespace std;

int main()
{
    int *p, i = 2;
    p = &i;
    cout << "location:" << p << " value:" << *p << endl;
    *p = 88; // set the value of location p with 88, while indirectily modify the value of i to 88
    cout << "location:" << p << " value:" << *p << endl;
    cout << "location:" << &i << " value:" << i << endl;

    // reference
    int &rei = i;
    cout << rei << " " << i << endl;
    // cout << &rei << " " << endl;
    // rei = 66;
    // cout << rei << " " << i << endl;
    // cout << &rei << " " << endl;
}