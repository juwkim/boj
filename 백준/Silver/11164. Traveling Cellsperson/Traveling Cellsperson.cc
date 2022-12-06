#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

char str[110];

int main()
{
    int t;
    scanf("%d",&t);
    while(t--)
    {
        int n,m;
        scanf("%d%d",&n,&m);
        for(int i=0;i<m;i++)
            scanf("%s",str);
        if(n>m) swap(n,m);
        if(n==1)
        {
            printf("%d\n",2*m-2);
        }
        else
        {
            if(n%2==0||m%2==0)
            {
                printf("%d\n",n*m);
            }
            else
            {
                printf("%d\n",m*n+1);
            }
        }
    }
    puts("LOL");
    return 0;
}