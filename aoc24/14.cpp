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

bool overlap(vector<robot> &R)
{
    for (int i = 0; i < R.size(); i++)
        for (int j = 0; j < i; j++)
            if (R[i].x == R[j].x && R[i].y == R[j].y)
                return true;
    return false;
}

void P1(vector<robot> &R)
{
    vector<int> counts(4);
    for (auto &r : R)
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

int main()
{
    vector<robot> R;
    char _;
    string line;
    while (getline(cin, line))
    {
        robot r;
        stringstream ss(line);
        ss >> _ >> _ >> r.x >> _ >> r.y >> _ >> _ >> r.vx >> _ >> r.vy;
        R.push_back(r);
    }
    for (int i = 1; i <= 10000; i++)
    {
        for (auto &r : R)
            r.move();
        if (i == 100)
            P1(R);
        if (!overlap(R))
            cout << i << "\n";
    }
}