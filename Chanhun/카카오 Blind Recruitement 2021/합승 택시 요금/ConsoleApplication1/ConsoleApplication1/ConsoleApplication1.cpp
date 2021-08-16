#include <iostream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

constexpr int MAX_VALUE = 0x00ffffff / 2;

int solution(int n, int s, int a, int b, vector<vector<int>> fares) {

    int answer = MAX_VALUE;

    // 노드는 1부터 최대 200이며, 편의상 노드는 0이 아닌 1부터 사용
    int cost[201][201];

    for (int y = 0; y < 201; ++y)
    {
        for (int x = 0; x < 201; ++x)
            cost[y][x] = MAX_VALUE;
    }

    for (int node = 1; node <= n; ++node)
    {
        // 자기 자신까지의 거리는 항상 0
        cost[node][node] = 0;
    }

    for (int index = 0; index < fares.size(); ++index)
    {
        int y = fares[index][0];
        int x = fares[index][1];
        int value = fares[index][2];

        // y->x , x->y 의 비용을 셋팅한다.
        cost[y][x] = cost[x][y] = value;
    }

    for (int mid = 1; mid <= n; ++mid)
    {
        for (int start = 1; start <= n; ++start)
        {
            for (int end = 1; end <= n; ++end)
            {
                // 거쳐갔을 때 비용이 더 적으면 거쳐갔을 때의 비용으로 변경한다.
                if (cost[start][end] > cost[start][mid] + cost[mid][end])
                    cost[start][end] = cost[start][mid] + cost[mid][end];
            }
        }
    }


    for (int node = 1; node <= n; ++node)
    {
        // s에서 node 까지 같이 타고, node에서 a,b 까지 각자 갔을 때의 비용을 계산한다.
        answer = min(answer, cost[s][node] + cost[node][a] + cost[node][b]);
    }

    return answer;
}


int main()
{
    std::cout << "Hello World!\n";
}
