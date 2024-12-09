#include "pch.h"

#include "MyLib.h"

// DLL internal state variables:
static unsigned long long previous_;  // Previous value, if any
static unsigned long long current_;   // Current sequence value
static unsigned index_;               // Current seq. position

double calculate(double x, double* arr, int n)
{
    double result = 0;
    for (int i = 0; i < n; ++i) {
        result += arr[i];
    }
    return result * x;
}

