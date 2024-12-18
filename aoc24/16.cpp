
#include <bits/stdc++.h>
using namespace std;
const int INF = 1e9;

vector<pair<int, int>> dirs{{1, 0}, {0, -1}, {-1, 0}, {0, 1}};

void P1(vector<string> &G, int r, int c, vector<vector<vector<int>>> &D)
{
    // dikstras algotithm
    priority_queue<array<int, 4>> Q;
    Q.push({0, r, c, 3});
    while (Q.size())
    {
        auto [t, r, c, d] = Q.top();
        Q.pop();
        if (D[r][c][d] < -t)
            continue;
        D[r][c][d] = -t;
        auto [dr, dc] = dirs[d];
        if (G[r + dr][c + dc] != '#' && D[r + dr][c + dc][d] > 1 - t) // move forwards
        {
            D[r + dr][c + dc][d] = 1 - t;
            Q.push({t - 1, r + dr, c + dc, d});
        }
        if (D[r][c][(d + 1) % 4] > 1000 - t) // turn left
        {
            D[r][c][(d + 1) % 4] = 1000 - t;
            Q.push({t - 1000, r, c, (d + 1) % 4});
        }
        if (D[r][c][(d + 3) % 4] > 1000 - t) // turn right
        {
            D[r][c][(d + 3) % 4] = 1000 - t;
            Q.push({t - 1000, r, c, (d + 3) % 4});
        }
    }
}

void P2(vector<string> &G, int r, int c, vector<vector<vector<int>>> &D, int T)
{
    // dfs now - pq not needed due
    vector<vector<bool>> O(D.size(), vector<bool>(D[0].size()));
    vector<array<int, 4>> Q;
    for (int dd = 0; dd < 4; dd++)
        Q.push_back({0, r, c, dd});
    int res = 0;
    while (Q.size())
    {
        auto [t, r, c, d] = Q.back();
        Q.pop_back();
        if (!O[r][c])
        {
            O[r][c] = true;
            res++;
        }
        auto [dr, dc] = dirs[d];
        if (G[r + dr][c + dc] != '#' && D[r + dr][c + dc][(d + 2) % 4] + 1 - t == T) // move forwards
        {
            D[r + dr][c + dc][d] = 1 - t;
            Q.push_back({t - 1, r + dr, c + dc, d});
        }
        if (D[r][c][(d + 3) % 4] + 1000 - t == T) // turn left
        {
            D[r][c][(d + 1) % 4] = 1000 - t;
            Q.push_back({t - 1000, r, c, (d + 1) % 4});
        }
        if (D[r][c][(d + 1) % 4] + 1000 - t == T) // turn right
        {
            D[r][c][(d + 3) % 4] = 1000 - t;
            Q.push_back({t - 1000, r, c, (d + 3) % 4});
        }
    }
    cout << res << "\n";
}

int main()
{
    string line;
    vector<string> G;
    while (getline(cin, line))
        G.push_back(line);
    int R = G.size();
    int C = G[0].size();
    int sr, sc, tr, tc;
    for (int r = 0; r < R; r++)
        for (int c = 0; c < C; c++)
        {
            if (G[r][c] == 'S')
            {
                sr = r;
                sc = c;
            }
            else if (G[r][c] == 'E')
            {
                tr = r;
                tc = c;
            }
        }
    vector<vector<vector<int>>> D(R, vector<vector<int>>(C, vector<int>(4, INF))), D_rev(R, vector<vector<int>>(C, vector<int>(4, INF)));

    P1(G, sr, sc, D);
    int res = min(min(D[tr][tc][0], D[tr][tc][1]), min(D[tr][tc][2], D[tr][tc][3]));
    cout << res << "\n";
    P2(G, tr, tc, D, res);
}