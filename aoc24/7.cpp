// clang-format off
#include <bits/stdc++.h>
using namespace std;
#define int long long
const int MOD = 998244353;
const int INF = 1e18; // 1e9
const int MAXBIT = 62; //30

vector<int> sorted(vector<int> a)
{
    sort(a.begin(),a.end());
    return a; 
}

bool increasing(vector<int> &a, bool strict = false)
{
    for (int i = 1; i < a.size(); i++)
    {
        if (strict && a[i] == a[i - 1])
            return false;
        if (a[i] < a[i - 1])
            return false;
    }
    return true;
}
bool decreasing(vector<int> &a, bool strict = false)
{
    for (int i = 1; i < a.size(); i++)
    {
        if (strict && a[i] == a[i - 1])
            return false;
        if (a[i] > a[i - 1])
            return false;
    }
    return true;
}



vector<pair<int, int>> neigh(int x, int y)
{
    vector<pair<int, int>> res;
    res.push_back({x + 1, y});
    res.push_back({x - 1, y});
    res.push_back({x, y + 1});
    res.push_back({x, y - 1});
    return res;
}

struct Node
{
    int val;
    Node *prev;
    Node *next;
    Node(int value) : val(value) {}
};

bool draw(vector<array<int, 2>> &v)
{
    int x = INF, y = INF, X = -INF, Y = -INF;
    for (auto a : v)
    {
        x = min(x, a[0]);
        X = max(X, a[0]);
        y = min(y, a[1]);
        Y = max(Y, a[1]);
    }
    int nY = Y - y + 1;
    int nX = X - x + 1;
    if (nY > 9)
        return false;
    vector<vector<bool>> G(nY, vector<bool>(nX));
    for (auto a : v)
    {
        G[a[1] - y][a[0] - x] = true;
    }
    for (int y = 0; y < nY; y++)
    {
        for (int x = 0; x < nX; x++)
        {
            cout << (G[y][x] ? "#" : " ");
        }
        cout << "\n";
    }
    cout << "\n\n";
    return true;
}
int which(int i, vector<int> &parent)
{
    if (i == parent[i])
        return i;
    return parent[i] = which(parent[i], parent);
}
void set_union(int i, int j, vector<int> &parent)
{
    i = which(i, parent);
    j = which(j, parent);

    if (i == j)
        return;
    parent[j] = i;
}
void jump_t(map<vector<int>, int> & seen, vector<int> & cur,  int &t , int N)
{
        if (seen.count(cur))
        {
            int p = seen[cur];
            int chunk = t - p;
            int rem = N - t;
            t += (rem / chunk) * chunk;
        }
        seen[cur] = t;
}


void draw(vector<vector<int>> &G)
{
    for (int y = 0; y < G.size(); y++)
    {
        for (int x = 0; x < G[y].size(); x++)
        {
            cout << G[y][x] << " ";
        }
        cout << "\n";
    }
    cout << "\n\n";
}
void draw(vector<vector<bool>> &G)
{
    for (int y = 0; y < G.size(); y++)
    {
        for (int x = 0; x < G[y].size(); x++)
        {
            cout << (G[y][x] ? "#" : " ");
        }
        cout << "\n";
    }
    cout << "\n\n";
    
}

#define dbg(x)cout<<(#x)<<": [";for(auto qq=x.begin();qq!=x.end();++qq)cout<<*qq<<(next(qq)!=x.end()?", ":"");cout<<"]\n"; // container 
#define mbg(x)cout<<(#x)<<": [";for(auto qq=x.begin();qq!=x.end();++qq)cout<<"("<<qq->first<<", "<<qq->second<<(next(qq)!=x.end()?"), ":")");cout<<"]\n"; // map or container<pair>
#define vbg(x)cout<<(#x)<<": [";for(auto qq=x.begin();qq!=x.end();++qq){cout<<"(";for(auto qqq=qq->begin();qqq!=qq->end();qqq++){cout<<*qqq<<(next(qqq)!=qq->end()?", ":"");};cout<<(next(qq)!=x.end()?"), ":")");};cout<<"]\n"; // vector of vectors
#define xbg(x)cout<<(#x)<<": "<<x<<"\n"; // for variables 
#define pbg(x)cout<<(#x)<<": ("<<x.first<<", "<<x.second<<")\n"; // for pairs
// clang-format on

bool valid(int X, vector<int> &a, int i)
{
    if (i == 0)
        return X == a[0];
    if (X % a[i] == 0)
        if (valid(X / a[i], a, i - 1))
            return true;
    return valid(X - a[i], a, i - 1);
}

void solve()
{
    int X, w, x, y, z, res = 0, res2 = 0, n, N = 1000, mx = -INF, mn = INF;
    map<int, int> m;
    // Node *node = new Node(0);
    // vector<vector<int>> G(N, vector<int>(N));
    string s, line;
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
    }

    // for (int i = 0; i < n; i++)

    cout << res << "\n";
}

signed main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
    return 0;
}