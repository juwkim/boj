#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
	int n;
	scanf("%d", &n);
	int xP[26], zP[26];
	for(int i = 0; i < n; ++i){
		int num;
		scanf("%d", &num);
		for(int j = 0; j < num; ++j){
			scanf("%d %d", &xP[i], &zP[i]);
		}
	}
	int p;
	scanf("%d", &p);
	int A[26], B[26], C[26];
	for(int i = 0; i < p; ++i){
		int x1, z1, x2, z2;
		scanf("%d %d %d %d", &x1, &z1, &x2, &z2);
		A[i] = z1 - z2, B[i] = x2 - x1, C[i] = x1 * z2 - z1 * x2;
		if (B[i] < 0) {
			A[i] = -A[i], B[i] = -B[i], C[i] = -C[i];
		}
	}

    int order[26];
	bool isDiv[27] = {0};
	isDiv[0] = 1, isDiv[n] = 1;
	for(int i = 0; i < n; i++) order[i] = i;
	for(int i = 0; i < p; i++){
		int pnc = 0;
		while(pnc < n){
			int next;
			for(int j = pnc + 1; ; ++j){
				if(isDiv[j]) {
					next = j;
					break;
				}
			}
			if(next == pnc + 1){
				pnc = next;
				continue;
			}
			int xianNo = 0;
			int tempHou[26];
			int houNo = 0;
			for(int j = 0; j < next - pnc; ++j){
				if (A[i] * xP[order[pnc+j]] + B[i] * zP[order[pnc+j]]+ C[i] > 0){
					order[pnc+xianNo] = order[pnc+j];
					xianNo ++;
				}
				else{
					tempHou[houNo] = order[pnc+j];
					houNo ++;
				}
			}
			isDiv[pnc+xianNo] = 1;
			for(int j = 0; j < houNo; j++){
				order[pnc+xianNo+j] = tempHou[j];
			}
			pnc = next;
		}
	}
	for(int i = 0; i < n; i++){
		printf("%c", order[i]+'A');
	}
	printf("\n");
	return 0;
}
