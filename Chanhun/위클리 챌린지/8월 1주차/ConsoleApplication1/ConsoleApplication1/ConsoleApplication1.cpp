#include <iostream>

using namespace std;

long long solution(int price, int money, int count)
{
    // int 사용시 오버플로우 발생 [ 64bit 데이터 타입 사용 ]
    long long answer = 0;

    for (int index = 1; index <= count; ++index)
    {
        answer += price * index;
    }

    if (answer > money)
    {
        return (long long)answer - money;
    }
    else
    {
        return 0;
    }
}

int main()
{

    return 1;
}