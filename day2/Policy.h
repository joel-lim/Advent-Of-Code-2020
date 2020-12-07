#include <string>

class Policy
{
private:
    int lower;
    int upper;
    char letter;

public:
    Policy(int lower_, int upper_, char letter_)
    {
        lower = lower_;
        upper = upper_;
        letter = letter_;
    }
    bool test1(std::string password);
    bool test2(std::string password);
};
