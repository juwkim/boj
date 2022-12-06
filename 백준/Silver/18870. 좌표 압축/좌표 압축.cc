#include <bits/stdc++.h>

#define rep(i,a,b) for(int i=(a);i<(b);++i)
#define all(x) (x).begin(), (x).end()
#define sz(x) (int)(x).size()
#define fastio ios::sync_with_stdio(0);cin.tie(0)
#define TS(x) #x
#define x first
#define y second
#define int long long
using namespace std;

using ll = long long;
using vi = vector<int>;
using pii = pair<int, int>;
const int MOD = 1e9+7;

signed main()
{
    fastio;
    int n;cin>>n;
    vi a(n);rep(i,0,n)cin>>a[i];
    vi pos(a);
    sort(all(pos));
    pos.erase(unique(all(pos)), pos.end());
    for(auto &x:a){
        cout<<(lower_bound(all(pos), x) - pos.begin())<<' ';
    }
    return 0;
}