#include <iostream>

using namespace std;
int l[26];
int main()
{
    char c;
    int mf=0;
    cin.get(c);
    while(c!='@')
    {
        if(((c>='a')&&(c<='z'))||((c>='A')&&(c<='Z')))
        {
            if((c>='a')&&(c<='z'))
            c-=32;
            l[c-65]++;
            if(l[c-65]>mf)mf=l[c-65];
        }
        cin.get(c);
    }
    for(int i=mf;i>=1;i--)
    {
        for(int j=0;j<26;j++)
            if(l[j]>=i)cout<<(char)(j+65);
            else cout<<" ";
        cout<<endl;
    }
    for(int i=1;i<=26;i++)cout<<'-';
    cout<<endl;
    for(int i=65;i<=65+25;i++)cout<<(char)i;
    cout<<endl;
    return 0;
}