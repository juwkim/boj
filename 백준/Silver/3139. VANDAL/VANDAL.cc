#include <iostream>

using namespace std;
int main()
{
   int N, R, S, D1, D2;
   cin >> N >> R >> S >> D1 >> D2;
   
   int cnt[2] = { 0, 0 };
   int s;
   for (int i = 1; i <= N; ++i)
   {
      ++cnt[(R+i)%2];
      if (i != R) ++cnt[(i+S)%2];

      s = D1 - i + 1;
      if (i != R && s != S && s >= 1 && s <= N) ++cnt[(D1+1)%2];

      s = D2 + i - N;
      if (i != R && s != S && s >= 1 && s <= N && i + s - 1 != D1) ++cnt[(D2+N)%2];
   }

   cout << cnt[0] + cnt[1] << '\n';
   cout << cnt[0] << ' ' << cnt[1] << '\n';
   return 0;
}