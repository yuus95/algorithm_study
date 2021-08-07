#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

bool cmp(const pair<string, int>& a, const pair<string, int>& b)
{
    return a.second > b.second;
}


vector<string> solution(vector<string> orders, vector<int> course)
{
    vector<string> answer;
    sort(orders.begin(), orders.end());

    for (int courseIndex = 0; courseIndex < course.size(); courseIndex++)
    {
        map<string, int> comb;

        for (int ordersIndex = 0; ordersIndex < orders.size(); ordersIndex++)
        {
            if (course[courseIndex] <= orders[ordersIndex].size())
            {
                vector<int> v;

                for (int k = 0; k < course[courseIndex]; k++)
                    v.push_back(1);

                for (int k = 0; k < orders[ordersIndex].size() - course[courseIndex]; k++)
                    v.push_back(0);

                // 순열을 사용하기 위한 정렬
                sort(v.begin(), v.end());

                do
                {
                    string str;

                    for (int k = 0; k < v.size(); k++)
                    {
                        // int 형 배열과 0,1 을 이용해서 순열을 사용한다.
                        if (v[k] == 1)
                            str += orders[ordersIndex][k];
                    }

                    sort(str.begin(), str.end());

                    comb[str] += 1;

                } while (next_permutation(v.begin(), v.end()));
            }
        }

        vector<pair<string, int>> vec(comb.begin(), comb.end());

        sort(vec.begin(), vec.end(), cmp);

        // 특정 개수의 메뉴중 가장 많이 주문한 문자열의 선택횟수를 구한다.
        int max = vec[0].second;

        if (max != 1)
        {
            for (auto m : vec)
            {
                // max 와 같으면 같은 개수의 메뉴라도 선택한다.
                if (max == m.second)
                    answer.push_back(m.first);
            }
        }
    }

    sort(answer.begin(), answer.end());

    return answer;
}


int main()
{


    return 1;
}