#include <bits/stdc++.h>
using namespace std;
#define int long long
int asum(int a, int n)
{
    int l = a + n - 1;
    return n * (a + l) / 2;
}

void P1(deque<pair<int, int>> Q)
{
    int res = 0;
    int pos = 0;
    int L = 0, R = Q.size() - 1;
    while (L <= R)
    {
        if (Q[R].second == -1 || Q[R].first == 0)
            R--;
        else if (Q[L].first == 0)
            L++;
        else if (Q[L].second == -1)
        { // blank space
            int d = min(Q[L].first, Q[R].first);
            res += Q[R].second * asum(pos, d);
            pos += d;
            Q[L].first -= d;
            Q[R].first -= d;
        }
        else
        {
            res += Q[L].second * asum(pos, Q[L].first);
            pos += Q[L].first;
            L++;
        }
    }
    cout << res << "\n";
}
void P2(vector<pair<int, int>> files, deque<pair<int, int>> spaces)
{
    int res = 0;
    for (int j = files.size() - 1; j >= 0; j--)
    {
        for (int i = 0; i < spaces.size(); i++)
        {
            if (spaces[i].first > files[j].first)
                break;
            if (spaces[i].second >= files[j].second)
            {
                files[j].first = spaces[i].first;
                spaces[i] = {spaces[i].first + files[j].second, spaces[i].second - files[j].second};
                break;
            }
        }

        auto [pos, d] = files[j];
        res += j * asum(pos, d);
    }
    cout << res << "\n";
}

void solve()
{
    int res = 0, res2 = 0;
    string s;
    getline(cin, s);
    deque<pair<int, int>> Q, spaces;
    vector<pair<int, int>> files(s.size() / 2 + 1); // id : pos,d
    int pos = 0;
    for (char c : s)
    {
        int file_id = (Q.size() % 2 == 0) ? Q.size() / 2 : -1;
        int d = c - '0';
        Q.push_back({d, file_id});
        if (file_id == -1)
            spaces.push_back({pos, d});
        else
            files[file_id] = {pos, d};
        pos += d;
    }

    P1(Q);
    P2(files, spaces);
}

signed main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
    return 0;
}