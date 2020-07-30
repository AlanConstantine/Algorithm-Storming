#include "Time.h"

Time::Time(int hour, int minute, int second){
    this->hour = hour;
    this->minute = minute;
    this->second = second;
}

int Time::getHour() const{
    return this->hour;
}