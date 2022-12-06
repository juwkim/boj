# [Silver V] Arithmetic Decoding - 21198 

[문제 링크](https://www.acmicpc.net/problem/21198) 

### 성능 요약

메모리: 113248 KB, 시간: 168 ms

### 분류

구현(implementation), 수학(math), 문자열(string)

### 문제 설명

<p>Arithmetic coding is a method to represent a message as a real number $x$ such that $0 \leq x < 1$. We will assume that the message consists only of uppercase 'A's and 'B's.  The two letters have associated probabilities $p_A$ and $p_B = 1 - p_A$ such that $0 < p_A < 1$.</p>

<p>The current interval $[a,b)$ is initially set to $[0,1)$ and we will update this interval one letter at a time.  To encode a letter, the current interval is divided into two subintervals as follows.  Let $c = a + p_A(b-a)$.  If the next letter is 'A', $[a,c)$ becomes the current interval.  Otherwise, the current interval is now $[c,b)$.  This process is repeated for each letter in the message.  If $[k,\ell)$ is the final interval, the encoded message is chosen to be $k$.</p>

<p>For example, if the original message is "ABAB" and $p_A = p_B = 0.5$, the sequence of intervals encountered in the algorithm is \[ [0,1) \xrightarrow{A} [0, 0.5) \xrightarrow{B} [0.25, 0.5) \xrightarrow{A} [0.25, 0.375) \xrightarrow{B} [0.3125, 0.375). \] The encoded message is therefore 0.3125, or 0.0101 in binary.</p>

<p>Given the length of the message, the probabilities, and the encoded message, determine the original message.</p>

### 입력 

 <p>The first line contains the integer $N$ ($1 \leq N \leq 15$), which is the length of the original message.  The second line contains the integer $D$ ($1 \leq D \leq 7$), which indicates that $p_A = \frac{D}{8}$. The third line contains the binary representation of the encoded message. It is guaranteed that the binary representation of the encoded message starts with "0." and contains at most $3N+2$ characters.</p>

<p>It is guaranteed that the encoded message came from an initial message of length $N$ consisting only of 'A' and 'B' using this value of $p_A$.</p>

### 출력 

 <p>Display the original message.</p>

