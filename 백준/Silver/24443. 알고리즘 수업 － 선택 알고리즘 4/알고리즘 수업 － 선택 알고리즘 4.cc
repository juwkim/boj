#include <bits/stdc++.h>

using namespace std;
vector<int> A(10000);

int linear_select(int i, int j, int k) {
    vector<int> nums(A.begin() + i, A.begin() + j + 1);
    std::nth_element(nums.begin(), nums.begin() + k - 1, nums.end());
    return nums.at(k - 1);
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(nullptr);
    int N, Q; cin >> N >> Q;
    for (int i = 0; i < N; ++i) cin >> A[i];
    while (Q--) {
        int op, i, j, k;
        cin >> op >> i >> j; --i; --j;
        if (op == 1) {
            cin >> k;
            cout << linear_select(i, j, k) << '\n';
        } else
            swap(A[i], A[j]);
    }
    return 0;
}