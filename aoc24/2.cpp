#include <bits/stdc++.h>
using namespace std;
#define int long long

bool increasing(vector<int> &a, bool strict = false)
{
    for (int i = 1; i < a.size(); i++)
    {
        if (strict && a[i] == a[i - 1])
            return false;
        if (a[i] < a[i - 1])
            return false;
    }
    return true;
}
bool decreasing(vector<int> &a, bool strict = false)
{
    for (int i = 1; i < a.size(); i++)
    {
        if (strict && a[i] == a[i - 1])
            return false;
        if (a[i] > a[i - 1])
            return false;
    }
    return true;
}
int max_dist(vector<int> &a)
{
    int mx = 0;
    for (int i = 1; i < a.size(); i++)
        mx = max(mx, abs(a[i] - a[i - 1]));
    return mx;
}

bool safe(vector<int> &a)
{
    return (increasing(a, true) || decreasing(a, true)) && (max_dist(a) <= 3);
}

bool safe(vector<int> &a, int j)
{
    vector<int> b;
    for (int i = 0; i < a.size(); i++)
        if (i != j)
            b.push_back(a[i]);
    return safe(b);
}
void solve()
{
    int x, res = 0, res2 = 0;
    string line;

    while (getline(cin, line))
    {
        vector<int> a, b;
        stringstream ss(line);
        while (ss >> x)
            a.push_back(x);

        if (safe(a))
        {
            res++;
            res2++;
            continue;
        }
        for (int i = 0; i < a.size(); i++)
            if (safe(a, i))
            {
                res2++;
                break;
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