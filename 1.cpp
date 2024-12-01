// clang-format off
#include <bits/stdc++.h>
using namespace std;
#define int long long
// clang-format on

void solve()
{
    int x, y, res = 0, res2 = 0;
    vector<int> a, b;
    map<int, int> m;
    string s, line;
    while (getline(cin, line))
    {
        stringstream ss(line);
        ss >> x >> y;
        a.push_back(x);
        b.push_back(y);
        m[y]++;
    }
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());
    for (int i = 0; i < a.size(); i++)
    {
        res += abs(a[i] - b[i]);
        res2 += a[i] * m[a[i]];
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