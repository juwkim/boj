#include "laugh.h"
#include <bits/stdc++.h>

using namespace std;
int longest_laugh(std::string s)
{
    int ans = 0;
    int cnt = 0;

    char prev = 0;
    for (auto cur: s)
    {
        if (prev == 'a')
        {
            if (cur == 'h')
            {
                cnt++;
            }
            else if (cur == 'a')
            {
                cnt = 1;
            }
            else
                cnt = 0;
        }
        else if (prev == 'h')
        {
            if (cur == 'a')
            {
                cnt++;
            }
            else if (cur == 'h')
            {
                cnt = 1;
            }
            else
                cnt = 0;
        }
        else if (cur == 'a' || cur == 'h')
            cnt = 1;
        prev = cur;
        ans = max(ans, cnt);
    }

	return ans;
}