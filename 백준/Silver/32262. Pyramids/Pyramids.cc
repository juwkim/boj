#include "pyramids.h"

std::vector<long long> a, b;
void init(std::vector<int> A, std::vector<int> B) {
    a.push_back(0); b.push_back(0);
    for (int num: A)
        a.push_back(a.back() + num);
    for (int num: B)
        b.push_back(b.back() + num);
}

bool can_transform(int L, int R, int X, int Y) {
  return (a[R + 1] - a[L]) == (b[Y + 1] - b[X]);
}