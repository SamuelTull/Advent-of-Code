#include <bits/stdc++.h>
using namespace std;
#define int long long

bool safe(vector<int> &a)
{
    bool inc = true, dec = true;
    for (int i = 1; i < a.size(); i++)
    {
        if (a[i] < a[i - 1])
            inc = false;
        if (a[i - 1] < a[i])
            dec = false;
        int d = abs(a[i] - a[i - 1]);
        if (d == 0 || d > 3)
            return false;
    }
    return inc || dec;
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