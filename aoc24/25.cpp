#include <bits/stdc++.h>
using namespace std;

void convert(vector<string> &cur, vector<array<int, 5>> &V)
{
    assert(cur[0].size() == 5);
    array<int, 5> v;
    for (int c = 0; c < 5; c++)
    {
        int i = 0;
        while (cur[i][c] == '#')
            i++;
        v[c] = i;
    }
    V.push_back(v);
}

bool ok(array<int, 5> &k, array<int, 5> &l)
{
    for (int c = 0; c < 5; c++)
    {
        if (k[c] + l[c] > 7)
            return false;
    }
    return true;
}

void solve()
{
    string line;
    vector<array<int, 5>> K, L;
    vector<string> cur;
    vector<vector<string>> groups = {{}};
    while (getline(cin, line))
    {
        if (line.empty())
        {
            assert(groups.back().size() == 7);
            groups.push_back({});
        }
        else
            groups.back().push_back(line);
    }

    for (vector<string> cur : groups)
    {
        if (cur[0] == ".....")
        {
            assert(cur[6] == "#####");
            reverse(cur.begin(), cur.end());
            convert(cur, K);
        }
        else
        {
            assert(cur[0] == "#####");
            assert(cur[6] == ".....");
            convert(cur, L);
        }
    }
    int res = 0;
    for (auto k : K)
        for (auto l : L)
            res += ok(k, l);
    cout << res << "\n";
}

signed main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
    return 0;
}