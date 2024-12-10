// clang-format off
#include <bits/stdc++.h>
using namespace std;
#define int long long
const int MOD = 998244353;
const int INF = 1e18; // 1e9
const int MAXBIT = 62; //30


#define dbg(x)cout<<(#x)<<": [";for(auto qq=x.begin();qq!=x.end();++qq)cout<<*qq<<(next(qq)!=x.end()?", ":"");cout<<"]\n"; // container 
#define mbg(x)cout<<(#x)<<": [";for(auto qq=x.begin();qq!=x.end();++qq)cout<<"("<<qq->first<<", "<<qq->second<<(next(qq)!=x.end()?"), ":")");cout<<"]\n"; // map or container<pair>
#define vbg(x)cout<<(#x)<<": [";for(auto qq=x.begin();qq!=x.end();++qq){cout<<"(";for(auto qqq=qq->begin();qqq!=qq->end();qqq++){cout<<*qqq<<(next(qqq)!=qq->end()?", ":"");};cout<<(next(qq)!=x.end()?"), ":")");};cout<<"]\n"; // vector of vectors
#define xbg(x)cout<<(#x)<<": "<<x<<"\n"; // for variables 
#define pbg(x)cout<<(#x)<<": ("<<x.first<<", "<<x.second<<")\n"; // for pairs
// clang-format on

vector<pair<int, int>> neigh(int x, int y)
{
    vector<pair<int, int>> res;
    res.push_back({x + 1, y});
    res.push_back({x - 1, y});
    res.push_back({x, y + 1});
    res.push_back({x, y - 1});
    return res;
}

bool inside(int r, int c, int R, int C)
{
    return r >= 0 && r < R && c >= 0 && c < C;
}

void solve()
{
    string s;
    vector<vector<int>> G;
    while (getline(cin, s))
    {
        vector<int> line;
        for (char c : s)
            line.push_back(c - '0');
        G.push_back(line);
    }

    int R = G.size();
    int C = G[0].size();
    vector<vector<set<pair<int, int>>>> P1(R, vector<set<pair<int, int>>>(C));
    vector<vector<int>> P2(R, vector<int>(C));
    vector<vector<bool>> vis(R, vector<bool>(C));

    deque<array<int, 2>> Q;
    for (int r = 0; r < R; r++)
        for (int c = 0; c < C; c++)
            if (G[r][c] == 0)
            {
                Q.push_back({r, c});
                P1[r][c].insert({r, c});
                P2[r][c] = 1;
            }

    while (Q.size())
    {
        auto [r, c] = Q.front();
        Q.pop_front();
        if (vis[r][c])
            continue;
        vis[r][c] = true;
        for (auto [nr, nc] : neigh(r, c))
            if (inside(nr, nc, R, C) && G[nr][nc] == G[r][c] + 1)
            {
                for (auto h : P1[r][c])
                    P1[nr][nc].insert(h);
                P2[nr][nc] += P2[r][c];
                Q.push_back({nr, nc});
            }
    }
    int res = 0, res2 = 0;
    for (int r = 0; r < R; r++)
        for (int c = 0; c < C; c++)
            if (G[r][c] == 9)
            {
                res += P1[r][c].size();
                res2 += P2[r][c];
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