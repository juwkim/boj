# [Bronze II] O Fortuna - 26505 

[문제 링크](https://www.acmicpc.net/problem/26505) 

### 성능 요약

메모리: 113112 KB, 시간: 108 ms

### 분류

런타임 전의 전처리(precomputation)

### 문제 설명

<p>In mathematics there are numbers that are fortunate, and some less fortunate. A fortunate number is defined as Q – P, where P is the product of the first N prime numbers (where N>1), and Q is the smallest prime greater than P+1. For example, if N = 2, P = 2*3 (the first two prime numbers), or 6. Q would be the smallest prime greater than 7, which is 11. Q – P is therefore 11 – 6, which is 5, another prime number. It has been conjectured by some mathematicians that this Fortunate number value will always be prime.</p>

<p>Likewise, a less fortunate number is defined as P – Q, using the same above scenario, except that Q is the largest prime less than P-1. Therefore, with N = 2, P again is 6, which makes Q = 3 (the largest prime less than 5), and so the LESS fortunate number in this case is 3. A similar conjecture for LESS fortunate numbers also asserts that they will always be prime.</p>

### 입력 

 <p>A row of integer values N in the range 1 < N <= 14.</p>

### 출력 

 <p>The original input value N, followed by the fortunate and less fortunate number, as described above, and shown below, with a single space separating each output item.</p>

