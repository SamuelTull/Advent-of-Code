#include <bits/stdc++.h>
using namespace std;
#define int long long
int INF = 1e18;

const vector<array<char, 3>> KEYPAD{{'7', '8', '9'}, {'4', '5', '6'}, {'1', '2', '3'}, {'X', '0', 'A'}};
const vector<array<char, 3>> DIRPAD{{'X', '^', 'A'}, {'<', 'v', '>'}};
vector<map<pair<char, char>, int>> MEMOS(30);
map<pair<char, char>, set<string>> DIRECTIONS;
vector<tuple<int, int, char>> DIRS{{1, 0, 'v'}, {-1, 0, '^'}, {0, 1, '>'}, {0, -1, '<'}};

void init(const vector<array<char, 3>> &PAD)
{
    for (int r = 0; r < PAD.size(); r++)
        for (int c = 0; c < PAD[r].size(); c++)
        {
            if (PAD[r][c] == 'X')
                continue;
            for (auto [dr, dc, d] : DIRS)
                for (auto [dr1, dc1, d1] : DIRS)

                    for (int t = 0; t < 5; t++)
                        for (int t1 = 0; t1 < 5; t1++)
                        {
                            int nr = r;
                            int nc = c;
                            bool ok = true;
                            string s = "";
                            for (int i = 0; i < t; i++)
                            {
                                nr += dr;
                                nc += dc;
                                s += d;
                                if (nr < 0 || nr >= PAD.size() || nc < 0 || nc >= PAD[nr].size() || PAD[nr][nc] == 'X')
                                    ok = false;
                            }
                            for (int i = 0; i < t1; i++)
                            {
                                nr += dr1;
                                nc += dc1;
                                s += d1;
                                if (nr < 0 || nr >= PAD.size() || nc < 0 || nc >= PAD[nr].size() || PAD[nr][nc] == 'X')
                                    ok = false;
                            }
                            if (ok)
                                DIRECTIONS[{PAD[r][c], PAD[nr][nc]}].insert(s + 'A');
                        }
        }
}

int move_robot(char s, char t, int rem)
{
    if (MEMOS[rem].count({s, t}))
        return MEMOS[rem][{s, t}];
    MEMOS[rem][{s, t}] = INF;

    for (string ops : DIRECTIONS[{s, t}])
    {
        int cur = 0;
        if (rem == 1)
            cur = ops.size();
        else
        {
            char u = 'A';
            for (char v : ops)
            {
                cur += move_robot(u, v, rem - 1);
                u = v;
            }
        }
        MEMOS[rem][{s, t}] = min(MEMOS[rem][{s, t}], cur);
    }
    return MEMOS[rem][{s, t}];
}

int move_arm(char s, char t)
{
    if (MEMOS[0].count({s, t}))
        return MEMOS[0][{s, t}];
    MEMOS[0][{s, t}] = INF;
    for (string ops : DIRECTIONS[{s, t}])
    {
        int cur = 0;
        char u = 'A';
        for (char v : ops)
        {
            cur += move_robot(u, v, 25);
            u = v;
        }
        MEMOS[0][{s, t}] = min(MEMOS[0][{s, t}], cur);
    }
    return MEMOS[0][{s, t}];
}

void solve()
{
    int res = 0;
    string s;
    while (getline(cin, s))
    {

        char u = 'A';
        int dig = stoi(s.substr(0, 3));
        for (char v : s)
        {
            res += dig * move_arm(u, v);
            u = v;
        }
    }
    cout << res << "\n";
}

signed main()
{
    init(KEYPAD);
    init(DIRPAD);
    solve();
    return 0;
}