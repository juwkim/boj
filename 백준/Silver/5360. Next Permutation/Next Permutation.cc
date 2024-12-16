#include <algorithm>
#include <iostream>
#include <string>
 
using namespace std;
int main()
{
    int n; cin >> n;
    string s;
    while (n--) {
        cin >> s;
        if (std::next_permutation(s.begin(), s.end()))
            cout << s;
        else
            cout << "USELESS";
        cout << '\n';
    }
}