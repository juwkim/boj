#include <cassert>
#include <cstdio>
#include <algorithm>

using namespace std;

int T, R, C, N;

int remove_tenants(int &K, int max_remove, int remove_cost) {
  int removed = min(K, max_remove);
  K -= removed;
  return removed * remove_cost;
}
int get_score(int all, int corners, int inners) {
  int sides = all - corners - inners;
  int K = R * C - N;
  int unhappiness = R * C * 2 - R - C;
  unhappiness -= remove_tenants(K,  inners, 4);
  unhappiness -= remove_tenants(K,   sides, 3);
  unhappiness -= remove_tenants(K, corners, 2);
  assert(K == 0);
  return unhappiness;
}

int min_unhappines() {
  // Guaranteed zero unhappiness.
  if (N <= (R * C + 1) / 2) return 0;

  if (R == 1) {
    int K = R * C - N;
    int unhappiness = C - 1;
    int remove_cost = 2;
    return unhappiness - K * remove_cost;
  }

  if (R % 2 == 1 && C % 2 == 1) {
    // 2.3.2
    // .4.4.
    // 3.4.3
    // .4.4.
    // 2.3.2
    int pattern1 = get_score(
      (R * C + 1) / 2,  // Max #tenants that can be removed.
      4,  // #tenants at the corners of the building.
      ((R-2) * (C-2) + 1) / 2  // #tenants at inner building.
    );

    // .3.3.
    // 3.4.3
    // .4.4.
    // 3.4.3
    // .3.3.
    int pattern2 = get_score(
      (R * C) / 2,  // Max #tenants that can be removed.
      0,  // #tenants at the corners of the building.
      ((R-2) * (C-2)) / 2  // #tenants at inner building.
    );

    return min(pattern1, pattern2);
  }

  // .3.2      2.3.      2.3.2
  // 3.4.  or  .4.3  or  .4.4.
  // .4.3      3.4.      3.4.3
  // 2.3.      .3.2      .3.3.
  return get_score(
    (R * C + 1) / 2,  // Max #tenants that can be removed.
    2,  // #tenants at the corners of the building.
    ((R-2) * (C-2) + 1) / 2  // #tenants at inner building.
  );
}

int main() {
  scanf("%d", &T);
  for (int TC = 1; TC <= T; TC++) {
    scanf("%d %d %d", &R, &C, &N);
    if (R > C) swap(R, C);
    printf("Case #%d: %d\n", TC, min_unhappines());
  }
}