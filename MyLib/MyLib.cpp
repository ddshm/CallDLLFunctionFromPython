#include "pch.h"
#include "MyLib.h"

double calculate(double x, double* arr, int n)
{
    double result = 0;
    for (int i = 0; i < n; ++i) {
        result += arr[i];
    }
    return result * x;
}
