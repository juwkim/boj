#include <bits/stdc++.h>
#define fastio ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
using namespace std;
#define all(v) (v).begin(), (v).end()
using ri = sregex_iterator;
int main() {
	fastio;
	string s, t;
	while (getline(cin, s) && s != "EOF") {
		//replace
		regex r(R"(dd|cei|ei|pink|EOF|.)");
        bool flag = 0;
		for (auto it = ri(all(s), r); it != ri(); it++) {
			string cur = it->str();
			if (cur == "dd") t += "p";
			else if (cur == "ei") t += "ie";
			else if (cur == "pink") t += "floyd";
            else if (cur == "EOF") { flag = 1; break; }
			else t += cur;
		}
		s = t, t.clear();

		for (auto i : s) if (islower(i) || i == ' ' || i == '\t' || i == '\r') t.push_back(i);
		s = t, t.clear();

		cout << s << '\n';
        if (flag) break;
	}
}