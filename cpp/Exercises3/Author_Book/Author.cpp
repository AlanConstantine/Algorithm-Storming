#include "Author.h"
#include <iostream>
using namespace std;

Author::Author(string name, string email, char gender): name(name), email(email), gender(gender) {};

string Author::getName() const { return name; }
string Author::getEmail() const { return email; }
char Author::getGender() const { return gender; }

void Author::setEmail(string email) { this->email = email; }
void Author::print() const {
    cout << "Email: " << email
         << ", Gender: " << gender
         << ", name:" << name << endl;
}