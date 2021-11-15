#include <iostream>
using namespace std;

int main()
{
    char ch1 = 'A';
    char *pc = &ch1;

    int i = 1;
    int *pi = &i;

    cout << "[1]" << endl;

    cout << &ch1 << endl; // get the location which is saving the value ch1;
    cout << *pc << endl;  // get the value (people who living in the room pc) saved in the location pc
    cout << pc << endl;   // show the location (the room number)

    cout << "location: " << pi << " or " << &i << " value: " << i << endl;

    int i2 = 2;
    *pi = i2; // put the value of i2 in the location pi
    cout << "The value of i: " << i << endl;
    cout << &i << ' ' << &i2 << endl;

    int i3 = *pi;
    cout << i3 << ' ' << &i3 << endl;

    int i4 = i;
    cout << i4 << &i4 << endl;

    pi = &i3; // make the pi point to the location of i3
    cout << pi << endl;

    cout << "[2]" << endl;

    char ch2 = *pc;
    cout << &ch2 << endl;
}