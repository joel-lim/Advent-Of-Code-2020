#include <string>
#include <algorithm>

#include "Policy.h"

bool Policy::test1(std::string password)
{
    int count = std::count(password.begin(), password.end(), letter);
    return lower <= count && count <= upper;
}

bool Policy::test2(std::string password)
{
    return (password.at(lower - 1) == letter) != (password.at(upper - 1) == letter);
}
