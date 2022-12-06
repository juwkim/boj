#include <bits/stdc++.h>
#include <fstream>
#include <iostream>
#include <string>

using namespace std;
int main()
{
    string line;
    while (true)
    {

        if (cin.eof() == true)
            break;
        getline(cin, line);
        for (string::iterator it = line.begin(); it != line.end(); )
        {
            int rep = 1;
            while (rep < 9 && (it + rep) != line.end() && *it == *(it + rep))
                ++rep;
            // A sequence of min(rep,9) identical characters starts at *it.
            if (rep > 1)
            {
                cout << rep << *it;
                it += rep;
            }
            else
            {
                cout << 1;
                for (; it != line.end() && ((it + 1) == line.end() || *it != *(it + 1)); ++it)
                {
                    cout << *it;
                    if (*it == '1')
                        cout << *it;
                }
                // Either a repetitive sequence begins at *it, or it reached the end of line.
                cout << 1;
            }
        }
        cout << endl;
    }
    return 0;
}
