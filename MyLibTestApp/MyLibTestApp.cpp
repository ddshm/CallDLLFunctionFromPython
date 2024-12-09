
#include <iostream>
#include <vector>
#include "MyLib.h"

int main()
{
    double x = 1.5;
    int n = 10;
    std::vector<double> arr(n, 2.5);
    double result = calculate(x, &(arr[0]), n);

    std::cout << "result = " << result << std::endl;
}