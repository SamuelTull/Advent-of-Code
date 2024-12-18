#include <bits/stdc++.h>
using namespace std;

void moveR(int &r, int &c, const vector<vector<bool>> &W, set<pair<int, int>> &B)
{
    vector<pair<int, int>> Q, to_move;
    int dc = 1;
    while (B.count({r, c + dc}))
    {
        to_move.push_back({r, c + dc});
        dc += 2;
    }
    if (B.size() && W[r][c + dc])
        return;
    for (auto p : to_move)
    {
        B.erase(p);
        auto [x, y] = p;
        B.insert({x, y + 1});
    }
    c++;
}

void moveL(int &r, int &c, const vector<vector<bool>> &W, set<pair<int, int>> &B)
{
    vector<pair<int, int>> Q, to_move;
    int dc = -2;
    while (B.count({r, c + dc}))
    {
        to_move.push_back({r, c + dc});
        dc -= 2;
    }
    if (B.size() && W[r][c + dc + 1])
        return;
    for (auto p : to_move)
    {
        B.erase(p);
        auto [x, y] = p;
        B.insert({x, y - 1});
    }
    c--;
}

void moveV(int dr, int &r, int &c, const vector<vector<bool>> &W, set<pair<int, int>> &B)
{
    set<pair<int, int>> to_move;
    vector<pair<int, int>> Q;

    if (B.count({r + dr, c}))
        Q.push_back({r + dr, c});
    if (B.count({r + dr, c - 1}))
        Q.push_back({r + dr, c - 1});

    if (!Q.size())
    {
        r += dr;
        return;
    }
    while (Q.size())
    {
        auto p = Q.back();
        Q.pop_back();
        if (to_move.count(p))
            continue;
        to_move.insert(p);
        auto [x, y] = p;

        if (W[x + dr][y] || W[x + dr][y + 1])
            return;
        for (int dy = -1; dy < 2; dy++)
            if (B.count({x + dr, y + dy}))
                Q.push_back({x + dr, y + dy});
    }

    for (auto p : to_move)
        B.erase(p);
    for (auto [x, y] : to_move)
        B.insert({x + dr, y});
    r += dr;
}

void move(char i, int &r, int &c, const vector<vector<bool>> &W, set<pair<int, int>> &B)
{
    map<char, pair<int, int>> m{
        {'^', {-1, 0}},
        {'>', {0, 1}},
        {'v', {1, 0}},
        {'<', {0, -1}},
    };
    auto [dr, dc] = m[i];
    if (W[r + dr][c + dc])
        return;
    if (dr == 0)
    {
        if (dc == 1)
            moveR(r, c, W, B);
        else
            moveL(r, c, W, B);
    }
    else
        moveV(dr, r, c, W, B);
}

void print(int r, int c, vector<vector<bool>> &W, set<pair<int, int>> &B)
{
    for (int i = 0; i < W.size(); i++)
    {
        for (int j = 0; j < W[0].size(); j++)
        {
            if (i == r && j == c)
                cout << '@';
            else if (W[i][j])
                cout << '#';
            else if (B.count({i, j}))
                cout << '[';
            else if (B.count({i, j - 1}))
                cout << ']';
            else
                cout << '.';
        }
        cout << "\n";
    }
}

void solve()
{
    int r, c, res = 0, res2 = 0, R = 0, C;
    string line;
    string I;
    vector<vector<bool>> W;
    set<pair<int, int>> B;
    bool instructions = false;
    while (getline(cin, line))
    {
        if (line.empty())
            instructions = true;
        else if (!instructions)
        {
            C = 0;
            W.push_back({});
            for (char i : line)
            {
                if (i == '@')
                {
                    r = R;
                    c = C;
                }
                W.back().push_back(i == '#');
                W.back().push_back(i == '#');
                if (i == 'O')
                {
                    B.insert({R, C});
                }
                C += 2;
            }
            R++;
        }
        else
            I += line;
    }
    int t = 0;
    for (char i : I)
        move(i, r, c, W, B);
    for (auto [i, j] : B)
        res += 100 * i + j;
    cout << res << "\n";
}

signed main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
    return 0;
}