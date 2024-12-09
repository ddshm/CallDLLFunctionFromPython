
#include <Windows.h>
#include <iostream>
#include <vector>


int main()
{
    HMODULE h = ::LoadLibraryA("MyLib.dll");
    if (h == NULL) {
        // failed to load dll
        return 1;
    }

    using MYLIB_CALC = double(__cdecl*)(double, double*, int);

    MYLIB_CALC mylib_calc_fn = (MYLIB_CALC)::GetProcAddress(h, "calculate");
    if (mylib_calc_fn == NULL) {
        // failed to get address of calculate function
        return 2;
    }

    double x = 1.5;
    int n = 10;
    std::vector<double> arr(n, 2.5);
    double result = (mylib_calc_fn)(x, &(arr[0]), n);

    std::cout << "result = " << result << std::endl;
    return 0;
}
