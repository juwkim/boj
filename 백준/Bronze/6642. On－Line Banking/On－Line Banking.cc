#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
using namespace std;

#define FOR(i,a,b) for(int i = (a); i < (b); ++i)
#define FOR2(i,a,b) for(int i = (a); i > (b); --i)
//#define FOR(i,b) for(int i = 0; i < (b); ++i)
#define FORTO(i,a,b) for(int i = (a); i <= (b); ++i)
#define FORD(i,b) for(int i = (b)-1; i >= 0; --i)
#define FOREACH(it,a) for(typeof((a).begin()) it = (a).begin(); it != (a).end(); ++it)

typedef long long ll;

#define $(x) int((x).size())

ll accounts[1000+100+47];

int main()
{
	while (1)
	{
		int cnt = 0;
		map<string, int> transl;
		
		int A;
		scanf("%d", &A);
		if (!A)
		{
			printf("goodbye\n");
			break;
		}
			
		char acc1[20], acc2[20];
		FOR(i, 0, A) //nacita bankove ucty
		{
			double in;
			ll balance;
			scanf(" %s %lf", acc1, &in);
			balance = in * 100.0 + 1e-9;
			
			transl[string(acc1)] = cnt;
			accounts[cnt] = balance;
			++cnt;
		}
		
		char command[20];
		while (1) //nacitava platobne prikazy
		{
			scanf(" %s", command);
			if (command[0] == 'e')
			{
				printf("end\n\n");
				break;
			}
			
			printf("%s", command);
			
			scanf(" %s", acc1);
			
			if (command[0] == 'c') //create
			{
				printf(": ");
				if (transl.find(string(acc1)) != transl.end())
					printf("already exists\n");
				else
				{
					transl[string(acc1)] = cnt;
					accounts[cnt] = 0;
					++cnt;
					printf("ok\n");
				}
			}
			else if (command[0] == 'd') //deposit
			{	
				ll balance;
				double in;
				scanf("%lf", &in);
				printf(" %.2lf: ", in);
				balance = in * 100.0 + 1e-9;
				
				if (transl.find(string(acc1)) == transl.end())
					printf("no such account\n");
				else
				{
					accounts[transl[acc1]] += balance;
					printf("ok\n");
				}
			}
			else if (command[0] == 'w') //withdraw
			{
				double in;
				ll balance;
				scanf("%lf", &in);
				printf(" %.2lf: ", in);
				balance = in * 100.0 + 1e-9;
				
				
				if (transl.find(string(acc1)) == transl.end())
					printf("no such account\n");
				else
				{
					int a = transl[acc1];
					if (accounts[a] < balance) 
						printf("insufficient funds\n");
					else
					{
						accounts[a] -= balance;
						printf("ok\n");
					}
				}
			}
			else //transfer
			{
				double in;
				ll balance;
				scanf(" %s %lf", acc2, &in);
				printf(" %.2lf: ", in);
				balance = in * 100.0 + 1e-9;
				
				if (transl.find(string(acc1)) == transl.end() ||
				   transl.find(string(acc2)) == transl.end())
					printf("no such account\n");
				else if (strcmp(acc1, acc2) == 0)
					printf("same account\n");
				else
				{
					int a = transl[acc1], b = transl[acc2];
					if (accounts[a] < balance)
						printf("insufficient funds\n");
					else
					{
						accounts[a] -= balance;
						accounts[b] += balance;
						if (acc1[5] == acc2[5])
							printf("ok\n");
						else 
							printf("interbank\n");
					}
				}
			}
		}
	}
	
	return 0;
}