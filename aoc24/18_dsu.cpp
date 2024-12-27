#include <bits/stdc++.h>
using namespace std;

pair<int, int> which(int r, int &c, vector<vector<pair<int, int>>> &parents)
{
    auto [pr, pc] = parents[r][c];
    if (pr != r || pc != c)
        parents[r][c] = which(pr, pc, parents);
    return parents[r][c];
}
void union_(int r, int c, int r2, int c2, vector<vector<pair<int, int>>> &parents, vector<vector<int>> &edges, vector<vector<int>> &size)
{
    bool pp = false;
    auto [root_r, root_c] = which(r, c, parents);
    auto [root_r2, root_c2] = which(r2, c2, parents);
    if (size[root_r2][root_c2] > size[root_r][root_c])
    {
        swap(root_r, root_r2);
        swap(root_c, root_c2);
    }
    parents[root_r2][root_c2] = {root_r, root_c};
    edges[root_r][root_c] |= edges[root_r2][root_c2];
    size[root_r][root_c] += size[root_r2][root_c2];
}

void solve()
{
    int r, c;
    vector<array<int, 2>> a;
    string s, line;
    char _;
    while (cin >> r >> _ >> c)
        a.push_back({r, c});
    int R = 71, C = 71;

    vector<vector<pair<int, int>>> parents(R, vector<pair<int, int>>(C));
    vector<vector<int>> edges(R, vector<int>(C)), size(R, vector<int>(C));

    for (int r = 0; r < R; r++)
    {
        edges[r][0] = 2;
        edges[r][C - 1] = 1;
    }
    for (int c = 0; c < C; c++)
    {
        edges[0][c] = 1;
        edges[R - 1][c] = 2;
    }

    for (auto [r, c] : a)
    {
        parents[r][c] = {r, c};
        size[r][c] = 1;
        for (int dr = -1; dr <= 1; dr++)
            for (int dc = -1; dc <= 1; dc++)
            {
                if (dc == 0 && dr == 0)
                    continue;
                int nr = r + dr;
                int nc = c + dc;
                if (nr < 0 || nr == R || nc < 0 || nc == C || size[nr][nc] == 0)
                    continue;
                union_(r, c, nr, nc, parents, edges, size);
                auto [pr, pc] = parents[r][c];
                if (edges[pr][pc] == 3) // top/right connects to left/bottom
                {
                    cout << r << "," << c;
                    return;
                }
            }
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
    return 0;
}