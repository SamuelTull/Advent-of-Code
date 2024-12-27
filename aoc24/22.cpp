#include <bits/stdc++.h>
using namespace std;

void mix(long long &x, long long y)
{
    x ^= y;
    x %= 16777216;
}

void update(long long &x)
{
    mix(x, x * 64);
    mix(x, x / 32);
    mix(x, x * 2048);
}

int main()
{
    long long x, res = 0;
    vector<int> m(130321);
    while (cin >> x)
    {
        int p = x % 10;
        int c = 0;
        vector<bool> seen(130321); // 19^4
        for (int i = 0; i < 2000; i++)
        {
            update(x);
            int d = (x % 10) - p + 9;
            p = x % 10;
            // d is in [-9,9]
            // d + 9 is in [0,18]
            c %= 6859; // 19 ^3
            c *= 19;
            c += d;
            if (i >= 3 && !seen[c])
            {
                seen[c] = true;
                m[c] += p;
            }
        }
        res += x;
    }

    cout << res << "\n"
         << *max_element(m.begin(), m.end()) << "\n";
    return 0;
}