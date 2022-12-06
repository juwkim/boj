#include <iostream>
#include <string>

using namespace std;
int is_exceed(string& str)
{
	unsigned len = str.size();
	if (len > 19) return 1;
	if (len < 19) return 0;
	return str.compare("9223372036854775807") > 0;
}

int main() {
	cin.tie(nullptr)->sync_with_stdio(false);

	long long a, b, r;

	string str1, str2;
	cin >> str1 >> str2 >> r;

	if (str1.compare("0") == 0 || str2.compare("0") == 0)
		cout << "0\n";
	else if (is_exceed(str1) || is_exceed(str2))
		cout << "overflow\n";
	else
	{
		a = stoll(str1, nullptr, 10);
		b = stoll(str2, nullptr, 10);
		if (a > r / b)
			cout << "overflow\n";
		else
			cout << a * b << "\n";
	}
	return 0;
}