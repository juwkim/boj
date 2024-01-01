#include <bits/stdc++.h>

using namespace std;
int A[10000];

int main() {
    ios_base::sync_with_stdio(false); cin.tie(nullptr);
    int N, Q; cin >> N >> Q;
    for (int i = 0; i < N; ++i) cin >> A[i];
    while (Q--) {
        int op, i, j, k;
        cin >> op >> i >> j; --i; --j;
        if (op == 1) {
            cin >> k; --k;
            vector<int> nums(A + i, A + j + 1);
            std::nth_element(nums.begin(), nums.begin() + k, nums.end());
            cout << nums[k] << '\n';
        } else
            swap(A[i], A[j]);
    }
    return 0;
}