#include <bits/stdc++.h>
using namespace std;

array<pair<int, int>, 4> neigh(int x, int y)
{
    return {
        pair<int, int>({x - 1, y}),
        pair<int, int>({x + 1, y}),
        pair<int, int>({x, y - 1}),
        pair<int, int>({x, y + 1}),
    };
}

void add_sides(int &sides, int r, int c, vector<string> &G, map<char, set<pair<int, int>>> &m)
{
    int R = G.size();
    int C = G[0].size();
    int S = G[r][c];

    if (r == 0 || G[r - 1][c] != S)
    {
        m['U'].insert({r, c});
        sides++;
        if (m['U'].count({r, c - 1}))
            sides--;
        if (m['U'].count({r, c + 1}))
            sides--;
    }

    if (r == R - 1 || G[r + 1][c] != S)
    {
        m['D'].insert({r, c});
        sides++;
        if (m['D'].count({r, c - 1}))
            sides--;
        if (m['D'].count({r, c + 1}))
            sides--;
    }

    if (c == 0 || G[r][c - 1] != S)
    {
        m['L'].insert({r, c});
        sides++;
        if (m['L'].count({r + 1, c}))
            sides--;
        if (m['L'].count({r - 1, c}))
            sides--;
    }

    if (c == C - 1 || G[r][c + 1] != S)
    {
        m['R'].insert({r, c});
        sides++;
        if (m['R'].count({r + 1, c}))
            sides--;
        if (m['R'].count({r - 1, c}))
            sides--;
    }
}

void solve()
{
    int res = 0, res2 = 0;
    string line;
    vector<string> G;
    while (getline(cin, line))
        G.push_back(line);
    int R = G.size(), C = G[0].size();
    vector<vector<bool>> seen(R, vector<bool>(C));

    for (int r = 0; r < R; r++)
        for (int c = 0; c < C; c++)
        {
            if (seen[r][c])
                continue;
            seen[r][c] = true;

            map<char, set<pair<int, int>>> m;

            int area = 0;
            int perimeter = 0;
            int sides = 0;

            deque<pair<int, int>> Q;
            Q.push_back({r, c});
            while (Q.size())
            {
                auto [cr, cc] = Q.front();
                Q.pop_front();
                add_sides(sides, cr, cc, G, m);
                area++;
                perimeter += 4;
                for (auto [nr, nc] : neigh(cr, cc))
                {
                    if (nr < 0 || nr >= R || nc < 0 || nc >= C || G[r][c] != G[nr][nc])
                        continue;
                    perimeter--;
                    if (!seen[nr][nc])
                    {
                        seen[nr][nc] = true;
                        Q.push_back({nr, nc});
                    }
                }
            }
            assert(perimeter == m['U'].size() + m['D'].size() + m['L'].size() + m['R'].size());
            res += area * perimeter;
            res2 += area * sides;
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