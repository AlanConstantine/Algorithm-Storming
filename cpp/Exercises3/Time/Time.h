#ifndef TIME_H
#define TIME_H
class Time {
    private:
        int hour;
        int minute;
        int second;
    public:
        Time(int hour, int minute, int second) {
            this->hour = hour;
            this->minute = minute;
            this->second = second;
        }

        int getHour() const;
        int getMinute() const;
        int getSecond() const;
        void setHour(int hour);
        void setMinute(int minute);
        void setSecond(int second);
        void setTime(int hour, int minute, int second);
        void print() const;
        void nextSecond();
};
#endif