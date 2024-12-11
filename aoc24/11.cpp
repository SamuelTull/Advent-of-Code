#include <bits/stdc++.h>
using namespace std;
#define int long long

map<pair<int, int>, int> MEMO;

int solve(int x, int t)
{
    if (t == 0)
        return 1;
    if (MEMO.count({x, t}))
        return MEMO[{x, t}];
    if (x == 0)
        return MEMO[{x, t}] = solve(1, t - 1);
    int dig = log10(x) + 1;
    if (dig % 2 == 0)
    {
        int p = pow(10, dig / 2);
        return MEMO[{x, t}] = solve(x / p, t - 1) + solve(x % p, t - 1);
    }
    return MEMO[{x, t}] = solve(x * 2024, t - 1);
}

void solve()
{
    int x, res = 0, res2 = 0;
    while (cin >> x)
    {
        res += solve(x, 25);
        res2 += solve(x, 75);
    }
    cout << res << "\n"
         << res2 << "\n";
}

signed main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
    return 0;
}