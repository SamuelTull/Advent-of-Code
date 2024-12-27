// clang-format off
#include <bits/stdc++.h>
using namespace std;
#define int long long
#define dbg(x)cout<<(#x)<<": [";for(auto qq=x.begin();qq!=x.end();++qq)cout<<*qq<<(next(qq)!=x.end()?", ":"");cout<<"]\n"; // container 
#define mbg(x)cout<<(#x)<<": [";for(auto qq=x.begin();qq!=x.end();++qq)cout<<"("<<qq->first<<", "<<qq->second<<(next(qq)!=x.end()?"), ":")");cout<<"]\n"; // map or container<pair>
#define vbg(x)cout<<(#x)<<": [";for(auto qq=x.begin();qq!=x.end();++qq){cout<<"(";for(auto qqq=qq->begin();qqq!=qq->end();qqq++){cout<<*qqq<<(next(qqq)!=qq->end()?", ":"");};cout<<(next(qq)!=x.end()?"), ":")");};cout<<"]\n"; // vector of vectors
#define xbg(x)cout<<(#x)<<": "<<x<<"\n"; // for variables 
#define pbg(x)cout<<(#x)<<": ("<<x.first<<", "<<x.second<<")\n"; // for pairs
// clang-format on

string move_arm(int s, int t)
{
    // 789
    // 456
    // 123
    // X0A
    // not 100% sure why this works, I originally thought we had to go R first and L last to avoid the empty square
    // then realised my answers were too long, it seems we should do < first then v then the other two
    // (probably because < is furthest from A and we always go there last)
    // this is fine unless the path would take us through the blank square
    // in which case we do the otehr path
    map<int, int> R{{7, 0}, {8, 0}, {9, 0}, {4, 1}, {5, 1}, {6, 1}, {1, 2}, {2, 2}, {3, 2}, {0, 3}, {-1, 3}};
    map<int, int> C{{7, 0}, {8, 1}, {9, 2}, {4, 0}, {5, 1}, {6, 2}, {1, 0}, {2, 1}, {3, 2}, {0, 1}, {-1, 2}};
    int dr = R[t] - R[s];
    int dc = C[t] - C[s];
    string res = "";
    // currently >^v<
    // want <v >^
    if (R[s] == 3 && C[t] == 0)
    {
        // up then left
        while (dr < 0)
        {
            dr++;
            res += '^';
        }
        while (dc < 0)
        {
            dc++;
            res += '<';
        }
        assert(dr == 0 && dc == 0);
    }
    if (C[s] == 0 && R[t] == 3)
    {
        // right then down
        while (dc > 0)
        {
            dc--;
            res += '>';
        }
        while (dr > 0)
        {
            dr--;
            res += 'v';
        }
        assert(dr == 0 && dc == 0);
    }

    while (dc < 0)
    {
        dc++;
        res += '<';
    }
    while (dr > 0)
    {
        dr--;
        res += 'v';
    }
    while (dc > 0)
    {
        dc--;
        res += '>';
    }
    while (dr < 0)
    {
        dr++;
        res += '^';
    }
    // go right first
    // go left last
    return res + 'A';
}

string move_robot(char s, char t)
{
    //     | ^ | A |
    // +---+---+---+
    // | < | v | > |
    // +---+---+---+
    // starts at A;
    // go right first
    // go left last
    map<char, int> R{{'^', 0}, {'A', 0}, {'<', 1}, {'v', 1}, {'>', 1}};
    map<char, int> C{{'^', 1}, {'A', 2}, {'<', 0}, {'v', 1}, {'>', 2}};

    int dr = R[t] - R[s];
    int dc = C[t] - C[s];
    string res = "";
    while (dc > 0)
    {
        dc--;
        res += '>';
    }
    while (dr > 0)
    {
        dr--;
        res += 'v';
    }
    while (dr < 0)
    {
        dr++;
        res += '^';
    }
    while (dc < 0)
    {
        dc++;
        res += '<';
    }
    return res + 'A';
}

void solve()
{
    int res = 0;
    string s;
    while (getline(cin, s))
    {
        int u = -1;
        string s2 = "";
        int dig = 0;
        for (char c : s)
        {
            int v = c == 'A' ? -1 : c - '0';
            if (v != -1)
            {
                dig *= 10;
                dig += v;
            }
            s2 += move_arm(u, v);
            u = v;
        }
        s = s2;
        for (int rep = 0; rep < 2; rep++)
        {
            s2 = "";
            char vv, uu = 'A';
            for (char vv : s)
            {
                s2 += move_robot(uu, vv);
                uu = vv;
            }
            s = s2;
        }
        res += dig * s.size();
    }
    xbg(res);
}

signed main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
    // solve2();
    return 0;
}