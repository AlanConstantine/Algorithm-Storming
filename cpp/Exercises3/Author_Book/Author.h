
#ifndef AUTHOR_H
#define AUTHOR_H
#include <string>
using namespace std;

class Author{
    private:
        string name;
        string email;
        char gender;
    
    public:
        Author(string name, string email, char gender);
        string getName() const;
        string getEmail() const;
        char getGender() const;
        void setEmail(string email);
        void print() const;
};

#endif 
// AUTHOR