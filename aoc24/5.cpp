#include <bits/stdc++.h>
using namespace std;

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

    auto compare = [&m](int x, int y)
    {
        // either x|y or y|x is in the instructions
        // either m[x].count(y) or m[y].count(x) is true
        return (m[x].count(y));
    };

    while (getline(cin, line))
    {
        stringstream ss(line);
        vector<int> a;
        while (ss >> x)
        {
            ss >> _;
            a.push_back(x);
        }

        n = a.size();

        if (is_sorted(a.begin(), a.end(), compare))
            res += a[n / 2];
        else
        {
            sort(a.begin(), a.end(), compare);
            res2 += a[n / 2];
        }
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