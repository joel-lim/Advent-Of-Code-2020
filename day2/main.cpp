#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <utility>

#include "Policy.h"

using std::cout;
using std::pair;
using std::string;
using std::vector;

vector<pair<Policy, string>> readFile(string filename);
int countTest1(vector<pair<Policy, string>> policyPasswords);
int countTest2(vector<pair<Policy, string>> policyPasswords);

int main(int argc, char **argv)
{
    vector<pair<Policy, string>> policyPasswords = readFile("input.txt");
    int count1 = 0;
    int count2 = 0;
    for (pair<Policy, string> policyPassword : policyPasswords)
    {
        if (std::get<0>(policyPassword).test1(std::get<1>(policyPassword)))
        {
            count1++;
        }
        if (std::get<0>(policyPassword).test2(std::get<1>(policyPassword)))
        {
            count2++;
        }
    }
    cout << "Part 1: " << count1 << "\n";
    cout << "Part 1: " << count2 << "\n";
    return 0;
}

vector<pair<Policy, string>> readFile(string filename)
{
    std::ifstream file(filename);
    string token;
    vector<pair<Policy, string>> policyPasswords;
    while (getline(file, token, '-'))
    {
        int lower = stoi(token);
        getline(file, token, ' ');
        int upper = stoi(token);
        getline(file, token, ':');
        char letter = token.at(0);
        getline(file, token, ' ');
        getline(file, token, '\n');
        string password = token;
        Policy policy(lower, upper, letter);
        pair<Policy, string> policyPassword(policy, password);
        policyPasswords.push_back(policyPassword);
    }
    return policyPasswords;
}
