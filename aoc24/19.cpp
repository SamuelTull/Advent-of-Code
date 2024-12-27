#include <bits/stdc++.h>
using namespace std;
#define int long long

map<int, int> memo;

int ok(string target, int i, vector<string> &towels)
{
    if (i == target.size())
        return 1;
    if (memo.count(i))
        return memo[i];
    int res = 0;
    for (string towel : towels)
    {
        if (target.substr(i, towel.size()) != towel)
            continue;
        res += ok(target, i + towel.size(), towels);
    }
    return memo[i] = res;
}

signed main()
{
    string s, line;
    vector<string> towels, targets;
    getline(cin, line);
    stringstream ss(line);
    while (ss >> s)
    {
        if (s.back() == ',')
            s = s.substr(0, s.size() - 1);
        towels.push_back(s);
    }
    while (getline(cin, line))
        if (!line.empty())
            targets.push_back(line);
    int res = 0, res2 = 0;
    for (auto target : targets)
    {
        memo.clear();
        int x = ok(target, 0, towels);
        res += x > 0;
        res2 += x;
    }
    cout << res << "\n"
         << res2;
    return 0;
}