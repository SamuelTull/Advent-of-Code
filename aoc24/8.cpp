#include <bits/stdc++.h>
using namespace std;

void solve()
{
    string line;
    vector<string> G;
    while (getline(cin, line))
        G.push_back(line);
    int R = G.size();
    int C = G[0].size();
    map<char, vector<pair<int, int>>> m;
    for (int r = 0; r < R; r++)
        for (int c = 0; c < C; c++)
            if (G[r][c] != '.')
                m[G[r][c]].push_back({r, c});

    set<pair<int, int>> s, s2;
    for (auto [c, ss] : m)
        for (int i = 0; i < ss.size(); i++)
            for (int j = i + 1; j < ss.size(); j++)
            {
                auto [r1, c1] = ss[i];
                auto [r2, c2] = ss[j];

                int dr = r2 - r1;
                int dc = c2 - c1;

                if (r1 - dr >= 0 && r1 - dr < R && c1 - dc >= 0 && c1 - dc < C)
                    s.insert({r1 - dr, c1 - dc});

                if (r2 + dr >= 0 && r2 + dr < R && c2 + dc >= 0 && c2 + dc < C)
                    s.insert({r2 + dr, c2 + dc});

                r2 = r1;
                c2 = c1;

                int l = gcd(dr, dc);
                dr /= l;
                dc /= l;

                while (r1 >= 0 && r1 < R && c1 >= 0 && c1 < C)
                {
                    s2.insert({r1, c1});
                    r1 -= dr;
                    c1 -= dc;
                }

                while (r2 >= 0 && r2 < R && c2 >= 0 && c2 < C)
                {
                    s2.insert({r2, c2});
                    r2 += dr;
                    c2 += dc;
                }
            }

    cout << s.size() << "\n";
    cout << s2.size() << "\n";
}

int main()
{
    solve();
    return 0;
}