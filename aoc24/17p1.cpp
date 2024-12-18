#include <bits/stdc++.h>
using namespace std;
#define int long long

signed main()
{
    int x;
    char _;
    array<int, 3> R;
    vector<int> P;
    cin >> R[0] >> R[1] >> R[2];
    while (cin >> x)
    {
        P.push_back(x);
        cin >> _;
    }
    int idx = 0;
    while (idx < P.size() - 1)
    {
        int a = P[idx], lit = P[idx + 1];
        int com = lit > 3 ? R[lit - 4] : lit;
        // cout << a << " " << lit << " " << com << "\n";
        idx += 2;
        if (a == 0)
            R[0] = R[0] / pow(2, com);
        else if (a == 1)
            R[1] ^= lit;
        else if (a == 2)
            R[1] = com % 8;
        else if (a == 3 && R[0] != 0)
            idx = lit;
        else if (a == 4)
            R[1] ^= R[2];
        else if (a == 5)
            cout << com % 8 << ", "[R[0] == 0];
        else if (a == 6)
            R[1] = R[0] / pow(2, com);
        else if (a == 7)
            R[2] = R[0] / pow(2, com);
    }
    return 0;
}