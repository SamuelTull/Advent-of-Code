#include <bits/stdc++.h>
using namespace std;

void topo(int x, vector<int> &b, map<int, set<int>> &m, map<int, int> &before)
{
    b.push_back(x);
    for (auto y : m[x])
    {
        if (before.count(y))
            if (--before[y] == 0)
                topo(y, b, m, before);
    }
}

void solve()
{
    int x, y, n, res = 0, res2 = 0;
    string s, line;
    char _;               // , and |
    map<int, set<int>> m; // x:v, all in v must be after x

    while (getline(cin, line))
    {
        if (line.empty())
            break;
        stringstream ss(line);
        ss >> x >> _ >> y;
        m[x].insert(y);
    }

    while (getline(cin, line))
    {
        stringstream ss(line);
        vector<int> a, b;
        map<int, int> before;
        while (ss >> x)
        {
            ss >> _;
            a.push_back(x);
            before[x] = 0;
        }
        for (auto [x, _] : before)
        {
            for (auto y : m[x])
                if (before.count(y))
                    before[y]++;
        }

        n = a.size();
        vector<int> starters;
        for (auto [x, v] : before)
            if (v == 0)
                starters.push_back(x);
        for (int x : starters)
            topo(x, b, m, before);
        if (a == b)
            res += a[n / 2];
        else
            res2 += b[n / 2];
    }

    cout << res << "\n";
    cout << res2 << "\n";
}

signed main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
    return 0;
}