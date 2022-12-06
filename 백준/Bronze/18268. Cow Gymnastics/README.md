# [Bronze I] Cow Gymnastics - 18268 

[문제 링크](https://www.acmicpc.net/problem/18268) 

### 성능 요약

메모리: 30852 KB, 시간: 72 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation)

### 문제 설명

In order to improve their physical fitness, the cows have taken up gymnastics!
Farmer John designates his favorite cow Bessie to coach the $N$ other cows and
to assess their progress as they learn various gymnastic skills.

<p>In each of $K$ practice sessions ($1 \leq K \leq 10$), Bessie ranks the $N$ cows according to their 
performance ($1 \leq N \leq 20$).  Afterward, she is curious about the consistency in these rankings.
A pair of two distinct cows is <em>consistent</em> if one cow did better than the
other one in every practice session.

</p><p>Help Bessie compute the total number of consistent pairs.
				</p>

### 입력 

 The first line of the input file contains two positive integers $K$ and $N$. The next $K$ lines will each contain the
integers $1 \ldots N$ in some order, indicating the rankings of the cows (cows
are identified by the numbers $1 \ldots N$). If $A$ appears before $B$ in one of
these lines, that means cow $A$ did better than cow $B$.

### 출력 

 Output, on a single line, the number of consistent pairs.

