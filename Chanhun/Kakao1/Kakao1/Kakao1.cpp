#include <iostream>
#include <string>

#include <vector>

using namespace std;

void sol_1(string& str)
{
    int size = str.length();
    for (int index = 0; index < size; ++index)
    {
        if (str[index] >= 'A' && str[index] <= 'Z')
        {
            str[index] = tolower(str[index]);
        }
    }

    return;
}

void sol_2(string& str)
{
    int size = str.length();
    for (int index = 0; index < size; ++index)
    {
        if ((str[index] >= 'a' && str[index] <= 'z') || (str[index] >= '0' && str[index] <= '9') || str[index] == '-' || str[index] == '_' || str[index] == '.')
            continue;

        str.erase(str.begin() + index);
        --size;
        --index;
    }

    return;
}

void sol_3(string& str)
{
    int size = str.length();


    while (str[0] == '.')
    {
        str.erase(str.begin());
        --size;
    }

    while (str[size - 1] == '.')
    {
        str.erase(str.begin() + (size - 1));
        --size;
    }

    for (int index = 0; index < size - 1; ++index)
    {
        if (str[index] == '.' && str[index + 1] == '.')
        {
            str.erase(str.begin() + index);
            --index;
            --size;
        }
    }

    return;
}

void sol_4(string& str)
{

    int size = str.length();

    for (int index = 0; index < size; ++index)
    {
        if (str[index] == ' ')
        {
            str[index] = 'a';
        }
    }

    return;
}

void sol_5(string& str)
{
    int size = str.length();

    if (size <= 15)
        return;

    str.erase(str.begin() + 15, str.end());

    sol_3(str);

    return;
}

void sol_6(string& str)
{
    int size = str.length();

    if (size > 2)
        return;

    if (size == 0)
    {
        str = "aaa";
        return;
    }

    for (int count = 0; count < 3 - size; ++count)
    {
        str += str[size - 1];
    }

    return;
}


string solution(string new_id) {

    sol_1(new_id);
    sol_2(new_id);
    sol_3(new_id);
    sol_4(new_id);
    sol_5(new_id);
    sol_6(new_id);


    return new_id;
}


int main()
{


    return 1;
}