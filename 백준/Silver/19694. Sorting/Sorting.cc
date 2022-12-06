#include "sorting.h"
#include <bits/stdc++.h>
using namespace std;

bool cmp(int a, int b){
    return compare_difficulty(a, b);
}
void sort_questions(int N, int Q, int A[]) {
	for (int i = 0; i < N; i++) A[i] = i + 1;
	sort(A, A + N, cmp);
	return;
}