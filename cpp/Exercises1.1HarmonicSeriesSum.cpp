#include <iostream>
using namespace std;

int main (){
    int n;
    cout << "Please enter n: ";
    cin >> n;
    cout << "Input n: " << n << endl;
    double harmonicSum = 0.0;
    int i = 1;
    while (i <= n){
        harmonicSum += double(1.0/i);
        ++i;
        // cout << "test: " << harmonicSum << endl;
    }
    cout << "The Harmonic sum is " << harmonicSum << endl;
}