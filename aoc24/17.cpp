#include <bits/stdc++.h>
using namespace std;

int out(long long a)
{
    long long x = (a % 8) ^ 5;
    long long y = a / pow(2, x);
    return (x ^ y ^ 6) % 8;
}

int main()
{
    int x;
    char _;
    vector<int> P;
    while (cin >> x)
    {
        P.push_back(x);
        cin >> _;
    }

    deque<pair<long long, int>> Q;
    for (int a = 0; a < 8; a++)
        Q.push_back({a, P.size() - 1});

    long long res = 1e18;
    while (Q.size())
    {
        auto [a, i] = Q.front();
        Q.pop_front();
        if (out(a) != P[i])
            continue;
        if (i == 0)
        {
            res = min(res, a);
            continue;
        }
        bool print = false;
        if (a == 192)
            print = true;
        a <<= 3;
        for (int b = 0; b < 8; b++)
            Q.push_back({a + b, i - 1});
    }
    cout << res;
    return 0;
}
