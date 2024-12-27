// clang-format off
#include <bits/stdc++.h>
using namespace std;
#define int long long

bool inside(int r, int c, int R, int C)
{
    return r >= 0 && r < R && c >= 0 && c < C;
}

vector<array<int, 2>> dirs{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

void solve()
{
    int R = 0, C, sr, sc, r, c;
    string line;
    vector<string> G;
    vector<vector<int>> path;
    while (getline(cin, line))
    {
        G.push_back(line);
        path.push_back(vector<int>(line.size()));
        for (int C = 0; C < G[R].size(); C++)
            if (G[R][C] == 'S')
            {
                sr = R;
                sc = C;
            }
        R++;
    }
    C = G[0].size();
    r = sr;
    c = sc;
    vector<array<int, 2>> P = {{r, c}};
    int cur = 1;
    path[r][c] = cur++;
    while (G[r][c] != 'E')
    {
        for (auto [dr, dc] : dirs)
        {
            int nr = r + dr;
            int nc = c + dc;
            if (!inside(nr, nc, R, C) || path[nr][nc] || G[nr][nc] == '#')
                continue;
            r = nr;
            c = nc;
            break;
        }
        P.push_back({r, c});
        path[r][c] = cur++;
    }
    int M = 100;
    int res = 0;
    for (auto [r, c] : P)
        for (auto [dr, dc] : dirs)
        {
            int nr = r + 2 * dr; // has to be straight or will be in wall
            int nc = c + 2 * dc;
            if (!inside(nr, nc, R, C))
                continue;
            int saved = path[nr][nc] - path[r][c] - 2;
            if (saved >= M)
                res++;
        }
    int res2 = 0;
    for (int i = 0; i < P.size(); i++)
    {
        auto [r, c] = P[i];
        for (int j = i + 100; j < P.size(); j++)
        {
            auto [r2, c2] = P[j];
            int dist = abs(r - r2) + abs(c - c2);
            if (dist <= 20 && path[r2][c2] - path[r][c] - dist >= M)
                res2++;
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