#include <iostream>
#include <vector>
#include <bitset>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int N, M;
    cin >> N >> M;
    
    vector<int> nums(N);
    for (int i = 0; i < N; ++i) {
        string s;
        cin >> s;
        int num = 0;
        for (char c : s) {
            num |= (1 << (c - 'a'));
        }
        nums[i] = num;
    }
    
    int cur = (1 << 26) - 1;
    for (int i = 0; i < M; ++i) {
        int o;
        char x;
        cin >> o >> x;
        int bit = 1 << (x - 'a');
        
        if (o == 1) {
            cur &= ~bit;
        } else {
            cur |= bit;
        }
        
        int ans = 0;
        for (int num : nums) {
            if ((cur & num) == num) {
                ++ans;
            }
        }
        cout << ans << '\n';
    }
    
    return 0;
}