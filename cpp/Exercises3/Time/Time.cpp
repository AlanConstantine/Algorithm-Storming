#include "Time.h"
#include <iostream>
#include <iomanip>
using namespace std;

// Time::Time(int hour, int minute, int second){
//     this->hour = hour;
//     this->minute = minute;
//     this->second = second;
// }

Time::Time(int hour, int minute, int second): hour(hour), minute(minute), second(second) {}

int Time::getHour() const{
    return this->hour;
}

int Time::getMinute() const{
    return this->minute;
}

int Time::getSecond() const{
    return this->second;
}

void Time::setHour(int hour) {
    this->hour = hour;
}

void Time::setMinute(int minute) {
    this->minute = minute;
}

void Time::setSecond(int second) {
    this->second = second;
}

void Time::nextSecond(){
    ++second;
    if (second > 59){
        second = 0;
        ++minute;
    };
    if (minute > 59){
        minute = 0;
        ++hour;
    }
    if (hour > 23){
        hour = 0;
    }

}

void Time::print() const {
    cout << setfill('0');
    cout << setw(2) << this->hour << ":"
         << setw(2) << this->minute << ":"
         << setw(2) << this->second
         << endl;
}