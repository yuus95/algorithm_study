#include <iostream>
#include <string>
#include <vector>

using namespace std;

void Match(int rotation, int row, int column, vector<vector<int>> key, int(*arr)[58])
{
    int size = key.size();

    switch (rotation)
    {
    // 0 도
    case 0:

        for (int y = 0; y < size; ++y)
        {
            for (int x = 0; x < size; ++x)
            {
                arr[y + row][x + column] += key[y][x];
            }
        }

        break;

    // 90도
    case 1:

        for (int y = 0; y < size; ++y)
        {
            for (int x = 0; x < size; ++x)
            {
                arr[y + row][x + column] += key[size - 1 - x][y];
            }
        }

        break;


    // 180도
    case 2:

        for (int y = 0; y < size; ++y)
        {
            for (int x = 0; x < size; ++x)
            {
                arr[y + row][x + column] += key[size - 1 - y][size - 1 - x];
            }
        }


        break;


    // 270도
    case 3:

        for (int y = 0; y < size; ++y)
        {
            for (int x = 0; x < size; ++x)
            {
                arr[y + row][x + column] += key[x][size - 1 - y];
            }
        }

        break;
    }

    return;
}

bool Check(int offset, int lockSize, int(*arr)[58])
{
    for (int y = offset; y < lockSize + offset; ++y)
    {
        for (int x = offset; x < lockSize + offset; ++x)
        {
            if (arr[y][x] != 1)
                return false;
        }
    }


    return true;
}


bool solution(vector<vector<int>> key, vector<vector<int>> lock) {

    int offset = key.size() - 1;


    for (int row = 0; row < lock.size() + offset; ++row)
    {
        for (int column = 0; column < lock.size() + offset; ++column)
        {
            for (int rotation = 0; rotation < 4; ++rotation)
            {
                // 최대 사이즈를 감안하여 생성
                int arr[58][58] = { 0, };

                for (int y = 0; y < lock.size(); ++y)
                {
                    for (int x = 0; x < lock.size(); ++x)
                    {
                        arr[offset + y][offset + x] = lock[y][x];
                    }
                }

                Match(rotation, row, column, key, arr);

                if (Check(offset, lock.size(), arr) == true)
                {
                    return true;
                }
            }
        }
    }


    return false;
}

int main()
{
    std::cout << "Hello World!\n";
}
