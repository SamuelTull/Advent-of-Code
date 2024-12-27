#include <bits/stdc++.h>
using namespace std;

void solve()
{
    string s;
    map<string, vector<string>> adj;
    while (getline(cin, s))
    {
        string u = s.substr(0, 2);
        string v = s.substr(3, 2);
        if (u[0] == 't')
            u[0] = 'T';
        if (v[0] == 't')
            v[0] = 'T';
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    int res = 0;
    for (const auto &P : adj)
    {
        string u = P.first;
        if (u[0] != 'T')
            continue;
        for (string v : adj[u])
        {
            if (v < u)
                continue;
            for (string w : adj[v])
            {
                if (w < v)
                    continue;
                for (string x : adj[w])
                    if (x == u)
                    {
                        res++;
                        break;
                    }
            }
        }
    }
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