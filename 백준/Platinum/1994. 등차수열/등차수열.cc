#include <bits/stdc++.h>

using namespace std;
int cache[5001][5001];
vector<int> nums;

int solve(int i, int j){
    if (i > j) return 0;
    else if (i == j) return 1;

    if (cache[i][j])
        return cache[i][j];
    int ret = 2;
    int diff = nums[j] - nums[i];
    int target = nums[j] + diff;

    int idx = lower_bound(nums.begin(), nums.end(), target) - nums.begin();
    if (nums[idx] == target)
        ret = solve(j, idx) + 1;
    cache[i][j] = ret;
    return ret;
}

int main(){
    cin.tie(nullptr)->sync_with_stdio(false);
    memset(cache, 0, sizeof(cache));

    int N; cin >> N;
    int K = N;
    while (K--) {
        int x; cin >> x;
        nums.push_back(x);
    }
    sort(nums.begin(), nums.end());

    int ans = 1;
    int cnt = 1;
    for (int i = 1; i <= N; i++){
        if (nums[i] == nums[i - 1]){
            ans = max(ans, ++cnt);
        }
        else cnt = 1;
    }
    
    nums.erase(unique(nums.begin(), nums.end()), nums.end());
    N = nums.size();
    for (int i = 0; i < N - 1; i++){
        for (int j = i + 1; j < N; j++){
            ans = max(ans, solve(i, j));
        }
    }

    cout << ans << '\n';
    return 0;
}