#ifndef POINT_H
#define POINT_H

class Point {
    private:
        int x, y;

    public:
        Point(int x, int y);
        int getX() const;
        int getY() const;
        void setX(int x);
        void setY(int y);
        void setXY(int x, int y);
        double getMagnitude() const;
        double getArgument() const;
        void print() const;

};

#endif