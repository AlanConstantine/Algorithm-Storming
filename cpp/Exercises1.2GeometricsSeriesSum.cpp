#include <iostream>
#include <math.h>
using namespace std;

int main(){
    int n;
    cout << "Please input n: ";
    cin >> n;

    double sum;
    int Geometor = 0;
    while (Geometor <= n){
        sum = sum + 1.0/pow(2, Geometor);
        ++Geometor;
    cout << "The Geometrics sum: " << sum << endl;
    }
}