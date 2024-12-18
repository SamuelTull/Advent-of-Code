#include <bits/stdc++.h>
using namespace std;
const int INF = 1e9;

vector<array<int, 2>> dirs{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

int bfs(int T, const vector<vector<int>> G)
{
    int R = G.size();
    int C = G[0].size();
    deque<array<int, 3>> Q;
    Q.push_back({0, 0, 0});
    vector<vector<bool>> seen(R, vector<bool>(C));
    seen[0][0] = true;
    while (Q.size())
    {
        auto [r, c, t] = Q.front();
        Q.pop_front();
        if (r == R - 1 && c == C - 1)
        {
            return t;
        }

        for (auto [dr, dc] : dirs)
        {
            int nr = r + dr;
            int nc = c + dc;
            if (nr < 0 || nr >= R || nc < 0 || nc >= C || G[nr][nc] <= T || seen[nr][nc])
                continue;
            seen[nr][nc] = true;
            Q.push_back({nr, nc, t + 1});
        }
    }
    return INF;
}

void solve()
{
    int r, c, w, x, y, z, res = 0, res2 = 0, n, N = 1000, mx = -INF, mn = INF;
    vector<array<int, 2>> a;
    string s, line;
    char _;
    while (cin >> r >> _ >> c)
        a.push_back({r, c});

    vector<vector<int>> G(71, vector<int>(71, INF));
    for (int i = 0; i < a.size(); i++)
        G[a[i][1]][a[i][0]] = i;

    cout << bfs(1024, G) << "\n";

    int L = 1024, R = a.size(), M;
    while (L < R)
    {
        int M = (L + R + 1) / 2;
        if (bfs(M, G) != INF)
            L = M;
        else
            R = M - 1;
    }
    cout << a[R + 1][0] << "," << a[R + 1][1] << "\n";
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
    return 0;
}