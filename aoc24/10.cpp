// clang-format off
#include <bits/stdc++.h>
using namespace std;
#define int long long
const int MOD = 998244353;
const int INF = 1e18; // 1e9
const int MAXBIT = 60;

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
    vector<vector<vector<int>>> P3(R, vector<vector<int>>(C, vector<int>(R * C / MAXBIT + 1)));
    vector<vector<bool>> vis(R, vector<bool>(C));

    deque<array<int, 2>> Q;

    int N_maps = 0;
    int cur_map = 0;

    for (int r = 0; r < R; r++)
        for (int c = 0; c < C; c++)
            if (G[r][c] == 0)
            {
                Q.push_back({r, c});
                P1[r][c].insert({r, c});
                P2[r][c] = 1;
                P3[r][c][N_maps] = 1LL << cur_map;
                if (cur_map == MAXBIT)
                {
                    N_maps++;
                    cur_map = 0;
                }
                else
                    cur_map++;
            }
    N_maps++;

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
                for (int ii = 0; ii < N_maps; ii++)
                    P3[nr][nc][ii] |= P3[r][c][ii];
            }
    }

    int res = 0, res2 = 0, res3 = 0;
    for (int r = 0; r < R; r++)
        for (int c = 0; c < C; c++)
        {
            if (G[r][c] == 9)
            {
                res += P1[r][c].size();
                res2 += P2[r][c];
                int sm = 0;
                for (int ii = 0; ii < N_maps; ii++)
                    sm += __builtin_popcountll(P3[r][c][ii]);
                res3 += sm;
            }
        }
    cout << res << "\n";
    cout << res2 << "\n";
    cout << res3 << "\n";
}

signed main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
    return 0;
}