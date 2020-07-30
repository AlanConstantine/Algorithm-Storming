#include "Circle.h"

Circle::Circle (double radius, string color) {
    this->radius = radius;
    this->color = color;
}

double Circle::getRadius() const{
    return radius;
}

void Circle::setRadius(double radius) {
    this->radius = radius;
}
string Circle::getColor() const{
    return color;
}

void Circle::setColor(string color) {
    this->color = color;
}

double Circle::getArea() const{
    return radius*radius*3.1415926;
}