// clang-format off
#include <bits/stdc++.h>
using namespace std;
#define int long long
const int MOD = 998244353;
const int INF = 1e18; // 1e9
const int MAXBIT = 62; //30

#define dbg(x)cout<<(#x)<<": [";for(auto qq=x.begin();qq!=x.end();++qq)cout<<*qq<<(next(qq)!=x.end()?", ":"");cout<<"]\n"; // container 
#define mbg(x)cout<<(#x)<<": [";for(auto qq=x.begin();qq!=x.end();++qq)cout<<"("<<qq->first<<", "<<qq->second<<(next(qq)!=x.end()?"), ":")");cout<<"]\n"; // map or container<pair>
#define vbg(x)cout<<(#x)<<": [";for(auto qq=x.begin();qq!=x.end();++qq){cout<<"(";for(auto qqq=qq->begin();qqq!=qq->end();qqq++){cout<<*qqq<<(next(qqq)!=qq->end()?", ":"");};cout<<(next(qq)!=x.end()?"), ":")");};cout<<"]\n"; // vector of vectors
#define xbg(x)cout<<(#x)<<": "<<x<<"\n"; // for variables 
#define pbg(x)cout<<(#x)<<": ("<<x.first<<", "<<x.second<<")\n"; // for pairs
// clang-format on

int to_int(map<string, bool> &M, char c)
{
    deque<array<string, 4>> Q;
    int res = 0;
    for (auto [s, x] : M)
    {
        if (!x || s[0] != c)
            continue;
        int b = 10 * (s[1] - '0') + (s[2] - '0');
        res += 1LL << b;
    }
    return res;
}

bool solve(map<string, bool> M, const vector<array<string, 4>> &A)
{
    deque<array<string, 4>> Q;
    for (auto &v : A)
        Q.push_back(v);

    int X = to_int(M, 'x');
    int Y = to_int(M, 'y');
    int Z = X + Y;
    int T = 0;

    bool ok = true;
    while (Q.size() && T++ < Q.size() + 5)
    {
        auto [x, op, y, z] = Q.front();
        Q.pop_front();
        if (!M.count(x) || !M.count(y))
        {
            Q.push_back({x, op, y, z});
            continue;
        }
        T = 0;

        assert(!M.count(z));
        if (op == "AND")
            M[z] = M[x] && M[y];
        else if (op == "OR")
            M[z] = M[x] || M[y];
        else if (op == "XOR")
            M[z] = M[x] ^ M[y];
        else
            assert(false);
        if (z[0] == 'z')
        {
            int b = 10 * (z[1] - '0') + (z[2] - '0');
            int res = (Z >> b) & 1;
            // cout << z << " " << res << " " << M[z] << " " << (res ^ M[z] == 1) << "\n";
            if (res ^ M[z] == 1)
                return false;
        }
    }
    return T == 0;
}

void check(set<string> &SWAPPED, vector<array<string, 4>> &ALL, char d, char d1)
{
    // find xii and yii ^ to something
    set<string> want{{'x', d, d1}, {'y', d, d1}};
    set<array<string, 4>> seen;
    string target;
    for (auto v : ALL)
    {
        if (want.count(v[0]))
        {
            seen.insert(v);
            if (v[1] == "XOR")
                target = v[3];
        }
    }
    for (int i = 0; i < ALL.size(); i++)
    {
        if (ALL[i][0] == target || ALL[i][2] == target)
        {
            seen.insert(ALL[i]);
            if (ALL[i][1] == "XOR" && ALL[i][3][0] != 'z')
            {
                for (int j = 0; j < ALL.size(); j++)
                {
                    if (ALL[j][3] == string({'z', d, d1}))
                    {
                        seen.insert(ALL[j]);
                        SWAPPED.insert(ALL[j][3]);
                        SWAPPED.insert(ALL[i][3]);
                        swap(ALL[i][3], ALL[j][3]);
                        return;
                    }
                }
            }
        }
    }
}

void solve()
{

    string s, line, x, op, y, z, _;
    map<string, bool> M;
    while (getline(cin, line))
    {
        if (line.empty())
            break;
        M[line.substr(0, 3)] = line[5] == '1';
    }
    vector<array<string, 4>> ALL, A, B, OK;
    // map<pair<string, string>, string> seen, seen2;
    while (getline(cin, line))
    {
        istringstream iss(line);
        iss >> x >> op >> y >> _ >> z;
        // seen[{x, y}] = op;
        // seen2[{x, y}] = z;
        ALL.push_back({x, op, y, z});
        // if (op != "XOR" && z[0] == 'z')
        //     A.push_back({x, op, y, z});
        // else if (op == "XOR" && z[0] != 'z')
        //     B.push_back({x, op, y, z});
        // else
        //     OK.push_back({x, op, y, z});
    }
    set<string> SWAPPED;

    for (char d = '0'; d <= '9'; d++)
        for (char d1 = '0'; d1 <= '9'; d1++)
        {
            if (!M.count({'x', d, d1}))
                continue;
            check(SWAPPED, ALL, d, d1);
        }

    for (int i = 0; i < ALL.size(); i++)
        for (int j = i + 1; j < ALL.size(); j++)
        {

            if (ALL[i][3][0] == 'z' || ALL[j][3][0] == 'z')
                continue;

            swap(ALL[i][3], ALL[j][3]);

            if (solve(M, ALL))
            {
                SWAPPED.insert(ALL[i][3]);
                SWAPPED.insert(ALL[j][3]);
            }

            swap(ALL[i][3], ALL[j][3]);
        }
    for (string s : SWAPPED)
        cout << s << ",";
    // vector<string> RES{"cph", "gws", "hgj", "nnt", "npf", "tss", "z13", "z19", "z33"};
    // vector<int> RES2;
    // for (string z : RES)
    // {
    //     for (int i = 0; i < ALL.size(); i++)
    //         if (ALL[i][3] == z)
    //             RES2.push_back(i);
    // }
    // dbg(RES2);
    // // 0 any, any
    // // abcdefgh
    // // 0a1a2a3a
    // vector<array<int, 8>> options;
    // int a = 0;
    // for (int b = a + 1; b < 8; b++)
    // {
    //     int c = 0;
    //     while (set<int>({a, b, c}).size() == 2)
    //         c++;
    //     for (int d = c + 1; d < 8; d++)
    //     {
    //         int e = 0;
    //         while (set<int>({a, b, c, d, e}).size() == 4)
    //             e++;
    //         for (int f = e + 1; f < 8; f++)
    //         {
    //             set<int> rem{0, 1, 2, 3, 4, 5, 6, 7, 8};
    //             rem.erase(a);
    //             rem.erase(b);
    //             rem.erase(c);
    //             rem.erase(d);
    //             rem.erase(e);
    //             rem.erase(f);
    //             int g = *rem.begin();
    //             int h = *rem.rbegin();
    //             // cout << a << b << c << d << e << f << g << h << "\n";
    //             options.push_back({a, b, c, d, e, f, g, h});
    //         }
    //     }
    // }
    // cout << options.size();

    // for (auto [a, b, c, d, e, f, g, h] : options)
    // {
    //     swap(ALL[RES2[a]][3], ALL[RES2[b]][3]);
    //     swap(ALL[RES2[c]][3], ALL[RES2[d]][3]);
    //     swap(ALL[RES2[e]][3], ALL[RES2[f]][3]);
    //     swap(ALL[RES2[g]][3], ALL[RES2[h]][3]);
    //     if (solve(M,ALL))
    //     swap(ALL[RES2[a]][3], ALL[RES2[b]][3]);
    //     swap(ALL[RES2[c]][3], ALL[RES2[d]][3]);
    //     swap(ALL[RES2[e]][3], ALL[RES2[f]][3]);
    //     swap(ALL[RES2[g]][3], ALL[RES2[h]][3]);
    // }
}

signed main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
    return 0;
}
