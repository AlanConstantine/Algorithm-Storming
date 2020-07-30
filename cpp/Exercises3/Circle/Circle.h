// #include <iostream>
#include <string>
using namespace std;

class Circle {
    private:
        double radius;
        string color;
    public:
        Circle(double radius = 1.0, string color = "red");
        double getRadius() const;
        void setRadius (double radius);
        string getColor() const;
        void setColor(string color);
        double getArea() const;
};