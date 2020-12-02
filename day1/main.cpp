#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <vector>

using namespace std;

vector<int> readFile(string filename);
void findPairSum(vector<int> expenses, int sum, int *num1, int *num2);

int main(int argc, char **argv)
{
    vector<int> expenses = readFile("input.txt");
    int num1;
    int num2;

    findPairSum(expenses, 2020, &num1, &num2);
    cout << "Part 1: " << num1 * num2 << "\n";

    set<int> expenseSet;
    for (int expense : expenses)
    {
        expenseSet.insert(expense);
    }
    for (int expense : expenses)
    {
        try
        {
            expenseSet.erase(expense);
            findPairSum(expenses, 2020 - expense, &num1, &num2);
            cout << "Part 2: " << num1 * num2 * expense << "\n";
            break;
        }
        catch (char const *)
        {
            continue;
        }
    }

    return 0;
}

vector<int> readFile(string filename)
{
    ifstream ExpenseFile(filename);
    string line;
    vector<int> expenses;
    while (getline(ExpenseFile, line))
    {
        expenses.push_back(stoi(line));
    }
    return expenses;
}

void findPairSum(vector<int> expenses, int sum, int *num1, int *num2)
{
    set<int> expenseSet;
    for (int expense : expenses)
    {
        int complement = sum - expense;
        if (expenseSet.find(complement) != expenseSet.end())
        {
            *num1 = expense;
            *num2 = complement;
            return;
        }
        expenseSet.insert(expense);
    }
    throw "No two entries summing to sum";
}
