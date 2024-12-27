#include <bits/stdc++.h>
using namespace std;

void print(vector<string> &x)
{
    int n = x.size();
    for (int i = 0; i < n; i++)
        cout << x[i] << ", "[i == n - 1];
}

int main()
{
    string s;
    map<string, set<string>> P, C;
    while (getline(cin, s))
    {
        string u = s.substr(0, 2);
        string v = s.substr(3, 2);
        if (u < v)
            swap(u, v);
        P[u].insert(v);
        C[v].insert(u);
    }
    vector<string> best;
    vector<vector<string>> Q;
    for (auto &p : C)
        Q.push_back({p.first});
    while (Q.size())
    {
        auto V = Q.back();
        Q.pop_back();
        if (V.size() > best.size())
            best = V;
        for (auto v : C[V.back()])
        {
            bool ok = true;
            for (auto p : V)
            {
                if (!P[v].count(p))
                {
                    ok = false;
                    break;
                }
            }
            if (ok)
            {
                V.push_back(v);
                Q.push_back(V);
                V.pop_back();
            }
        }
    }
    print(best);
    return 0;
}
