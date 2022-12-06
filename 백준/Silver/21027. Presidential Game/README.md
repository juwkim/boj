# [Silver V] Presidential Game - 21027 

[문제 링크](https://www.acmicpc.net/problem/21027) 

### 성능 요약

메모리: 113248 KB, 시간: 108 ms

### 분류

애드 혹(ad_hoc), 수학(math)

### 문제 설명

<p>Two candidates are running for this year’s presidential election, John Wee and Preston Wo. Taking a break from promoting their campaign, they decide to play a game with an array $A$ of $N$ integers. The candidates will make alternating moves until there is a single element left, starting with John as the current president.</p>

<p>In each turn, John will choose a contiguous subarray (containing between $2$ to $K$ elements, inclusive) from $A$ and replace the subarray with a single element, which is the sum of all the elements in the subarray. In each turn, Preston will choose a contiguous subarray (containing between $2$ to $K$ elements, inclusive) from $A$ and replace the subarray with a single element, which is the bitwise XOR of all the elements in the subarray. The bitwise XOR of an array of integers $X$ is defined as follows, where $\oplus$ denotes the bitwise XOR notation.</p>

<p>$$XOR(X) = \begin{cases} X_1 \oplus X_2 & \text{if }|X| = 2 \\ XOR([X_1, X_2, \dots, X_{|X|-1}]) \oplus X_{|X|} & \text{if }|X| > 2 \end{cases}$$</p>

<p>Since John is the candidate with number 1, John is the winner of the game if the single element left in the array is an odd number. Otherwise, Preston is the winner of the game if the single element left in the array is an even number. You want to predict who will win the game if both candidates play optimally.</p>

### 입력 

 <p>Input begins with a line containing two integers: $N$ $K$ ($2 \le K \le N \le 1000$) representing the length of the array and the maximum length of the chosen subarray for each turn, respectively. The next line contains $N$ integers: $A_i$ ($0 \le A_i \le 1000$) representing the given array $A$.</p>

### 출력 

 <p>Output in a line a string representing the winner of the game, either <code>John</code> or <code>Preston</code>.</p>

