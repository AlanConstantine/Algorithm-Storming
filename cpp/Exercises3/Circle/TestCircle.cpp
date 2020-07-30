#include <iostream>
#include "Circle.h"
using namespace std;

int main() {
    Circle c1(1.2, "red");
    cout << "Current area: " << c1.getArea() << endl; 
    return 0;
}