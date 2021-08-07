#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <unordered_map>
#include <algorithm>

using namespace std;

void AddCase(string* s, int score, unordered_map<string, vector<int>>& scores)
{
    vector<int> v = { 0,0,0,0 };

    for (int count = 4; count >= 0; --count)
    {
        if (count != 4)
            v[count] = 1;

        do
        {
            string str;

            for (int index = 0; index < 4; ++index)
            {
                if (v[index] == 1)
                {
                    str += s[index];
                }
                else
                {
                    str += '-';
                }
            }

            scores[str].push_back(score);

        } while (next_permutation(v.begin(), v.end()));

        sort(v.begin(), v.end());
    }

    return;
}

vector<int> solution(vector<string> info, vector<string> query) {

    unordered_map<string, vector<int>> scores;

    vector<int> answer;
    string s[4];
    string str;

    for (int index = 0; index < info.size(); ++index)
    {
        istringstream stt(info[index]);
        stt >> s[0] >> s[1] >> s[2] >> s[3] >> str;
        AddCase(s, stoi(str), scores);
    }

    auto iterE = scores.end();
    for (auto iter = scores.begin(); iter != iterE; ++iter)
    {
        sort(iter->second.begin(), iter->second.end());
    }

    for (int index = 0; index < query.size(); ++index)
    {
        int score;
        istringstream stt(query[index]);
        stt >> s[0] >> str >> s[1] >> str >> s[2] >> str >> s[3] >> str;


        score = stoi(str);

        vector<int>& v = scores[s[0] + s[1] + s[2] + s[3]];
        if (v.size() != 0)
        {
            auto iter = lower_bound(v.begin(), v.end(), score);
            answer.push_back(v.size() - (iter - v.begin()));
        }
        else
        {
            answer.push_back(0);
        }
    }

    return answer;
}



int main()
{
    vector<int> v;

    v.push_back(1);
    v.push_back(2);
    v.push_back(3);
    v.push_back(4);
    v.push_back(5);

    auto num = lower_bound(v.begin(), v.end(), 3);

    cout << num - v.begin();

    return 0;
}



