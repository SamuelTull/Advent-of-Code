#include <bits/stdc++.h>
using namespace std;

map<char, pair<int, int>> m{
    {'^', {-1, 0}},
    {'>', {0, 1}},
    {'v', {1, 0}},
    {'<', {0, -1}},
};

void move(char i, int &r, int &c, vector<string> &G)
{
    auto [dr, dc] = m[i];
    int steps = 1;
    while (G[r + steps * dr][c + steps * dc] == 'O')
        steps++;
    if (G[r + steps * dr][c + steps * dc] == '#')
        return;
    if (steps > 1)
    {
        swap(G[r + dr][c + dc], G[r + steps * dr][c + steps * dc]);
    }
    r += dr;
    c += dc;
}

pair<int, int> start(vector<string> &G)
{
    for (int r = 0; r < G.size(); r++)
        for (int c = 0; c < G[0].size(); c++)
            if (G[r][c] == '@')
                return {r, c};
    return {0, 0};
}

int main()
{
    int res = 0, res2 = 0;
    string line;
    string I;
    vector<string> G;
    bool instructions = false;
    while (getline(cin, line))
    {
        if (line.empty())
            instructions = true;
        else if (!instructions)
            G.push_back(line);
        else
            I += line;
    }
    int R = G.size();
    int C = G[0].size();
    auto [r, c] = start(G);

    for (char i : I)
        move(i, r, c, G);

    for (r = 0; r < R; r++)
        for (c = 0; c < C; c++)
            if (G[r][c] == 'O')
                res += 100 * r + c;
    cout << res << "\n";
}