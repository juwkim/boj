#include <cstdio>
#include <cstring>

typedef long long ll;

char str[50];

int main() {
  ll s = 0;
  for (;;) {
    ll ei, ed;
    if (scanf("%lld.%lld\n", &ei, &ed) != 2)
      break;
    s += ei * 100 + ed;
  }
  sprintf(str, "%03lld", s);
  int l = strlen(str);
  str[l+1] = 0;
  str[l] = str[l-1];
  str[l-1] = str[l-2];
  str[l-2] = '.';
  printf("%s\n", str);
  return 0;
}