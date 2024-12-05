#include <bits/stdc++.h>
using namespace std;

int solve(vector<string> &G, int r, int c)
{
    int res = 0;
    int R = G.size(), C = G[0].size();
    vector<array<int, 2>> DIRS = {{1, 0}, {0, 1}, {1, 1}, {-1, 1}}; // {| _ / \} check for XMAS and SAMX
    for (auto [dr, dc] : DIRS)
    {
        string cur = {G[r][c]};
        for (int i = 1; i < 4; i++)
        {
            int nr = r + i * dr;
            int nc = c + i * dc;
            if (!(nr >= 0 && nr < R && nc >= 0 && nc < C))
                break;
            cur += G[nr][nc];
        }
        if (cur == "XMAS" || cur == "SAMX")
            res++;
    }
    return res;
}

int solve2(vector<string> &G, int r, int c)
{
    int R = G.size(), C = G[0].size();
    if (r == 0 || r == R - 1 || c == 0 || c == C - 1)
        return 0;
    if (G[r][c] != 'A')
        return 0;
    string a = {G[r - 1][c - 1], G[r + 1][c + 1]};
    string b = {G[r + 1][c - 1], G[r - 1][c + 1]};
    return (a == "MS" || a == "SM") && (b == "MS" || b == "SM");
}

void solve()
{
    int res = 0, res2 = 0;
    vector<string> G;
    string line;

    while (getline(cin, line))
        G.push_back(line);

    int R = G.size(), C = G[0].size();

    for (int r = 0; r < R; r++)
    {
        for (int c = 0; c < C; c++)
        {
            res += solve(G, r, c);
            res2 += solve2(G, r, c);
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