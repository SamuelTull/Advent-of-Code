#include <bits/stdc++.h>
using namespace std;

bool valid(long long X, vector<int> &a, int i)
{
    if (i == 0)
        return X == a[0];
    if (a[i] > X)
        return false;
    if (X % a[i] == 0)
        if (valid(X / a[i], a, i - 1))
            return true;
    return valid(X - a[i], a, i - 1);
}

bool valid2(long long X, vector<int> &a, int i)
{
    if (i == 0)
        return X == a[0];
    if (a[i] > X)
        return false;
    int n_dig = (int)log10(a[i]) + 1;
    int d = pow(10, n_dig);
    if (X % d == a[i] && valid2(X / d, a, i - 1)) // concatenation
        return true;
    if (X % a[i] == 0 && valid2(X / a[i], a, i - 1)) // multiplication
        return true;
    if (valid2(X - a[i], a, i - 1)) // addition
        return true;
    return false;
}

void solve()
{
    long long X, x;
    long long res = 0, res2 = 0;
    string line;
    char _;
    while (getline(cin, line))
    {
        stringstream ss(line);
        ss >> X >> _;
        vector<int> a;
        while (ss >> x)
            a.push_back(x);

        if (valid(X, a, a.size() - 1))
            res += X;
        else if (valid2(X, a, a.size() - 1))
            res2 += X;
    }

    cout << res << "\n";
    cout << res + res2 << "\n";
}

signed main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
    return 0;
}