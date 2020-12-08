#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <utility>

#include "Map.h"

using std::cout;
using std::pair;
using std::string;
using std::vector;

Map readFile(string filename);

int main(int argc, char **argv)
{
    Map map = readFile("input.txt");
    cout << "Part 1: " << map.traverse(3, 1) << "\n";

    long long part2 = 1;
    part2 *= map.traverse(1, 1);
    part2 *= map.traverse(3, 1);
    part2 *= map.traverse(5, 1);
    part2 *= map.traverse(7, 1);
    part2 *= map.traverse(1, 2);
    cout << "Part 2: " << part2 << "\n";
    return 0;
}

Map readFile(string filename)
{
    std::ifstream file(filename);
    vector<string> rows;
    string line;
    while (getline(file, line))
    {
        rows.push_back(line);
    }
    Map map(rows);
    return map;
}
