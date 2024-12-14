#include <bits/stdc++.h>
using namespace std;

int X = 101;
int Y = 103;

struct robot
{
    int x, y, vx, vy;
    void move()
    {
        x = (x + vx + X) % X;
        y = (y + vy + Y) % Y;
        // cout << x << " " << y << "\n";
    }

    int quadrant()
    {
        if (x == X / 2 || y == Y / 2)
            return -1;
        int quad = 0;
        if (x < X / 2)
            quad++;
        if (y < Y / 2)
            quad += 2;
        return quad;
    }
};

void print(vector<robot> &a)
{
    vector<string> G(Y, string(X, ' '));
    for (auto &r : a)
        G[r.y][r.x] = '#';

    for (int y = 0; y < Y; y++)
        cout << G[y] << "\n";
}

bool overlap(vector<robot> &a)
{
    for (int i = 0; i < a.size(); i++)
        for (int j = 0; j < i; j++)
            if (a[i].x == a[j].x && a[i].y == a[j].y)
                return true;
    return false;
}

void solve()
{
    vector<robot> a;
    char _;
    string line;
    while (getline(cin, line))
    {
        robot r;
        stringstream ss(line);
        ss >> _ >> _ >> r.x >> _ >> r.y >> _ >> _ >> r.vx >> _ >> r.vy;
        a.push_back(r);
    }

    int N = 500;
    for (int i = 1; i <= 10000; i++)
    {

        for (auto &r : a)
            r.move();
        if (i == 100)
        {
            vector<int> counts(4);
            for (auto &r : a)
            {
                int quad = r.quadrant();
                if (quad != -1)
                    counts[quad]++;
            }
            long long res = 1;
            for (int x : counts)
                res *= x;
            cout << res << "\n";
        }
        if (!overlap(a))
        {
            cout << i << "\n";
            print(a);
        }
    }
}

signed main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
    return 0;
}