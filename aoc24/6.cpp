#include <bits/stdc++.h>
using namespace std;

pair<int, int> find_start(vector<string> &G)
{
    for (int r = 0; r < G.size(); r++)
        for (int c = 0; c < G[r].size(); c++)
            if (G[r][c] == '^')
                return {r, c};
    return {-1, -1};
}

vector<pair<int, int>> DIRS = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

void search(int r, int c, int d, vector<string> &G, vector<vector<bool>> &seen)
{
    seen[r][c] = true;
    auto [dr, dc] = DIRS[d];
    int nr = r + dr;
    int nc = c + dc;
    if (!(nr >= 0 && nr < G.size() && nc >= 0 && nc < G[0].size()))
        return;
    if (G[nr][nc] == '#')
        search(r, c, (d + 1) % 4, G, seen);
    else
        search(nr, nc, d, G, seen);
}

bool search(int r, int c, int d, vector<string> &G, vector<vector<array<bool, 4>>> &seen)
{
    auto [dr, dc] = DIRS[d];
    int nr = r + dr;
    int nc = c + dc;
    if (!(nr >= 0 && nr < G.size() && nc >= 0 && nc < G[0].size()))
        return false;
    if (G[nr][nc] == '#')
    {
        if (seen[r][c][d])
            return true;
        seen[r][c][d] = true;
        return search(r, c, (d + 1) % 4, G, seen);
    }
    return search(nr, nc, d, G, seen);
}

void solve()
{
    vector<string> G;
    string line;
    while (getline(cin, line))
        G.push_back(line);
    int R = G.size();
    int C = G[0].size();
    auto [sr, sc] = find_start(G);
    vector<vector<bool>> seen(R, vector<bool>(C));
    search(sr, sc, 0, G, seen);
    int res = 0, res2 = 0;
    for (int r = 0; r < R; r++)
        for (int c = 0; c < C; c++)
            if (seen[r][c])
            {
                res++;
                G[r][c] = '#';
                vector<vector<array<bool, 4>>> seen2(R, vector<array<bool, 4>>(C));
                if (r != sr || c != sc)
                    res2 += search(sr, sc, 0, G, seen2);
                G[r][c] = '.';
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