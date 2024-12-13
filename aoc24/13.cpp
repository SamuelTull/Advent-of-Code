#include <bits/stdc++.h>
using namespace std;

void solve()
{
    int ax, ay, bx, by;
    long long X, Y;
    vector<long long> res(2);
    while (cin >> ax >> ay >> bx >> by >> X >> Y)
    {
        for (int rep = 0; rep < 2; rep++)
        {
            long long b = (Y * ax - X * ay) / (by * ax - bx * ay);
            long long a = (X - b * bx) / ax;
            if (a * ax + b * bx == X && a * ay + b * by == Y)
                res[rep] += 3 * a + b;
            X += 10000000000000;
            Y += 10000000000000;
        }
    }
    cout << res[0] << "\n"
         << res[1] << "\n";
}

signed main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
    return 0;
}