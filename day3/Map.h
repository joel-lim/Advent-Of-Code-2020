#include <string>
#include <vector>

using std::string;
using std::vector;

class Map
{
private:
    vector<string> rows;

public:
    Map(vector<string> rows_)
    {
        rows = rows_;
    }
    int traverse(int right, int down);
};
