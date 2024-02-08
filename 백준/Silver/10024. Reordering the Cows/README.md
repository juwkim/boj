# [Silver III] Reordering the Cows - 10024 

[문제 링크](https://www.acmicpc.net/problem/10024) 

### 성능 요약

메모리: 108080 KB, 시간: 108 ms

### 분류

구현, 순열 사이클 분할

### 제출 일자

2024년 2월 8일 12:57:50

### 문제 설명

<p>Farmer John's N cows (1 <= N <= 100), conveniently numbered 1..N, are standing in a row.  Their ordering is described by an array A, where A(i) is the number of the cow in position i.  Farmer John wants to rearrange them into a different ordering for a group photo, described by an array B, where B(i) is the number of the cow that should end up in position i.</p><p>For example, suppose the cows start out ordered as follows:</p><p>A = 5 1 4 2 3</p><p>and suppose Farmer John would like them instead to be ordered like this:</p><p>B = 2 5 3 1 4</p><p>To re-arrange themselves from the "A" ordering to the "B" ordering, the cows perform a number of "cyclic" shifts.  Each of these cyclic shifts begins with a cow moving to her proper location in the "B" ordering, displacing another cow, who then moves to her proper location, displacing another cow, and so on, until eventually a cow ends up in the position initially occupied by the first cow on the cycle.  For example, in the ordering above, if we start a cycle with cow 5, then cow 5 would move to position 2, displacing cow 1, who moves to position 4, displacing cow 2, who moves to position 1, ending the cycle.  The cows keep performing cyclic shifts until every cow eventually ends up in her proper location in the "B" ordering.  Observe that each cow participates in exactly one cyclic shift, unless she occupies the same position in the "A" and "B" orderings.</p><p>Please compute the number of different cyclic shifts, as well as the length of the longest cyclic shift, as the cows rearrange themselves.</p>

### 입력 

 <ul><li>Line 1: The integer N.</li><li>Lines 2..1+N: Line i+1 contains the integer A(i).</li><li>Lines 2+N..1+2N: Line 1+N+i contains the integer B(i).</li></ul>

### 출력 

 <ul><li>Line 1: Two space-separated integers, the first giving the number of cyclic shifts and the second giving the number cows involved in the longest such shift.  If there are no cyclic shifts, output -1 for the second number.</li></ul>

