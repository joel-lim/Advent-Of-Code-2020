#include <string>

#include "Map.h"

using std::string;

int Map::traverse(int right, int down)
{
    int no_trees = 0;
    int height = rows.size();
    int width = rows.at(0).length();
    int x = 0;
    for (int y = 0; y < height; y += down)
    {
        if (rows.at(y)[x] == '#')
        {
            no_trees++;
        }
        x = (x + right) % width;
    }
    return no_trees;
}
