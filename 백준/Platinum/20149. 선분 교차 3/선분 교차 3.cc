#include <bits/stdc++.h>
 
using namespace std;
 
#define ll long long

pair<ll, ll> xy[4];
pair<double, double> p;

int ccw(pair<ll, ll> p1, pair<ll, ll> p2, pair<ll, ll> p3)
{
    ll temp = p1.first * p2.second + p2.first * p3.second + p3.first * p1.second;
 
    temp = temp - p1.second * p2.first - p2.second * p3.first - p3.second * p1.first;
 
    return (temp > 0) - (temp < 0);
}
 
int chk(int abc, int abd, int cda, int cdb)
{
    if (abc * abd == 0 && cda * cdb == 0)
    {
        if (xy[0] <= xy[3] && xy[2] <= xy[1])
            return 1;
        else
            return 0;
    }

    if (abc * abd <= 0 && cda * cdb <= 0)
        return 2;
    else
        return 0;
}

pair<double, double> get_point(pair<ll, ll> p1, pair<ll, ll> p2, pair<ll, ll> p3, pair<ll, ll> p4) {

    pair<double, double> ans;
    if ((p2.first - p1.first) && (p4.first - p3.first)) {
        double a = (p2.second - p1.second) / (double) (p2.first - p1.first);
        double b = (p4.second - p3.second) / (double) (p4.first - p3.first);
        ans.first = (a * p1.first - b * p3.first + p3.second - p1.second) / (double) (a - b);
        ans.second = a * (ans.first - p1.first) + p1.second;
    }
    else if (p2.first - p1.first) {
        ans.first = p3.first;
        double a = (p2.second - p1.second) / (double) (p2.first - p1.first);
        ans.second = a * (ans.first - p1.first) + p1.second;
    }
    else {
        ans.first = p1.first;
        double b = (p4.second - p3.second) / (double) (p4.first - p3.first);
        ans.second = b * (ans.first - p3.first) + p3.second;
    }
    return ans;
}

int main(void)
{

    for (int i = 0; i < 4; i++)
        scanf("%lld %lld", &xy[i].first, &xy[i].second);
    
    if (xy[0] > xy[1]) swap(xy[0], xy[1]);
    if (xy[2] > xy[3]) swap(xy[2], xy[3]);

    int abc = ccw(xy[0], xy[1], xy[2]);
    int abd = ccw(xy[0], xy[1], xy[3]);
    int cda = ccw(xy[2], xy[3], xy[0]);
    int cdb = ccw(xy[2], xy[3], xy[1]);
    switch (chk(abc, abd, cda, cdb)) {
        case 0:
            printf("0\n");
            break;
        case 1:
            if (xy[0] == xy[3])
                printf("1\n%lld %lld\n", xy[0].first, xy[0].second);
            else if (xy[1] == xy[2])
                printf("1\n%lld %lld\n", xy[1].first, xy[1].second);
            else if ((abc == 0) && (abd == 0) && (cda == 0) && (cdb == 0))
                printf("1\n");
            else if (xy[0] == xy[2])
                printf("1\n%lld %lld\n", xy[0].first, xy[0].second);
            else
                printf("1\n%lld %lld\n", xy[1].first, xy[1].second);
            break;
        default:
            p = get_point(xy[0], xy[1], xy[2], xy[3]);
            printf("1\n%.16f %.16f\n", p.first, p.second);
            break;
    }
    return 0;
}