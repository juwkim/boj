#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int N, A, B, M;
    cin >> N >> A >> B >> M;
    vector<int> dorm(N+1);
    for (int i = 1; i <= N; i++) dorm[i] = i;
    
    vector<int> score(N+1);
    vector<bool> happy(M+1);
    if (A-1 <= B) happy[1] = true;
    for (int i = 2; i <= M; i++) {
        for (int j = 1; j <= N; j++) {
            cin >> score[j];
        }
        for (int j = 1; j <= N; j++) {
            int x;
            cin >> x;
            score[j] -= x;
        }
        for (int j = 1; j <= N-1; j++) {
            if (score[dorm[j]] >= 0 && score[dorm[j+1]] >= 0) {
                if (score[dorm[j+1]]-score[dorm[j]] >= 2) {
                    swap(dorm[j], dorm[j+1]);
                    score[dorm[j]] -= 2;
                    score[dorm[j+1]] += 2;
                }
            } else if (score[dorm[j]] >= 0 && score[dorm[j+1]] < 0) {
            } else if (score[dorm[j]] < 0 && score[dorm[j+1]] >= 0) {
                swap(dorm[j], dorm[j+1]);
                score[dorm[j]] -= 2;
                score[dorm[j+1]] += 2;
            } else {
                if (score[dorm[j+1]]-score[dorm[j]] >= 4) {
                    swap(dorm[j], dorm[j+1]);
                    score[dorm[j]] -= 2;
                    score[dorm[j+1]] += 2;
                }
            }
        }
        int x = 0, y = 0;
        for (int j = 1; j <= N; j++) {
            if (dorm[j] == 1) {
                x = j;
            } else if (dorm[j] == A) {
                y = j;
            }
        }
        int diff = abs(x - y);
        if (diff <= B) {
            happy[i] = true;
        }
    }
    cout << count(happy.begin(), happy.end(), true) << ' ';
    int ans = 0, cnt = 0;
    for (int i = 1; i <= M; i++) {
        if (happy[i]) {
            ++cnt;
        } else {
            ans = max(ans, cnt);
            cnt = 0;
        }
    }
    ans = max(ans, cnt);
    cout << ans << '\n';
    return 0;
}