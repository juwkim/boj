# [Silver IV] Alternative Scale of Notation - 7397 

[문제 링크](https://www.acmicpc.net/problem/7397) 

### 성능 요약

메모리: 113248 KB, 시간: 112 ms

### 분류

임의 정밀도 / 큰 수 연산(arbitrary_precision), 수학(math), 정수론(number_theory)

### 문제 설명

<p>One may define a map of strings over an alphabet \(\Sigma_B = \{C_1, C_2, \dots, C_B\}\) of size $B$ to non-negative integer numbers, using characters as digits $C_1 = 0, C_2 = 1, \dots , C_B = B − 1$ and interpreting the string as the representation of some number in a scale of notation with base $B$. Let us denote this map by $U_B$, for a string $\alpha[1..n]$ of length $n$ we put \[U_B(\alpha) = \sum_{i=0}^{n-1}{\alpha[n-i]\cdot B^i}\text{.}\]</p>

<p>For example, $U_3(1001) = 1 \cdot 27 + 0 \cdot 9 + 0 \cdot 3 + 1 \cdot 1 = 28$.</p>

<p>However, this correspondence has one major drawback: it is not one-to-one. For example, $$28 = U_3(1001) = U_3(01001) = U_3(001001) = \dots \text{,}$$ infinitely many strings map to the number $28$.</p>

<p>In mathematical logic and computer science this may be unacceptable. To overcome this problem, the alternative interpretation is used. Let us interpret characters as digits, but in a slightly different way: $C_1 = 1, C_2 = 2, \dots , C_B = B$. Note that now we do not have $0$ digit, but rather we have a rudiment $B$ digit. Now we define the map $V_B$ in a similar way, for each string $\alpha[1..n]$ of length $n$ we put \[V_B(\alpha) = \sum_{i=0}^{n-1}{\alpha[n-i]\cdot B^i}\text{.}\]</p>

<p>For an empty string $\epsilon$ we put $V_B(\epsilon) = 0$.</p>

<p>This map looks very much like UB, however, the set of digits is now different. So, for example, we have $V_3(1313) = 1 \cdot 27 + 3 \cdot 9 + 1 \cdot 3 + 3 \cdot 1 = 60$.</p>

<p>It can be easily proved that the correspondence defined by this map is one-to-one and onto. Such a map is called <em>bijective</em>, and it is well known that every bijective map has an inverse. Your task in this problem is to compute the inverse for the map $V_B$. That is, for a given integer number $x$ you have to find the string $\alpha$, such that $V_B(\alpha) = x$.</p>

### 입력 

 <p>The first line of the input file contains $B$ ($2 \le B \le 9$). The second line contains an integer number $x$ given in a usual decimal scale of notation, $0 \le x \le 10^{100}$.</p>

### 출력 

 <p>Output such string $\alpha$, consisting only of digits from the set $\{1, 2, \dots , B\}$, that $V_B(\alpha) = x$.</p>

