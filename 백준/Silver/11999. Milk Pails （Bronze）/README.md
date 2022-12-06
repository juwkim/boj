# [Silver V] Milk Pails (Bronze) - 11999 

[문제 링크](https://www.acmicpc.net/problem/11999) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

브루트포스 알고리즘(bruteforcing), 수학(math)

### 문제 설명

<p>Farmer John has received an order for exactly \(M\) units of milk (\(1 \leq M \leq 1,000\)) that he needs to fill right away. Unfortunately, his fancy milking machine has just become broken, and all he has are three milk pails of integer sizes \(X\), \(Y\), and \(M\) (\(1 \leq X < Y < M\)). All three pails are initially empty. Using these three pails, he can perform any number of the following two types of operations:</p>

<p>- He can fill the smallest pail (of size \(X\)) completely to the top with \(X\) units of milk and pour it into the size-\(M\) pail, as long as this will not cause the size-\(M\) pail to overflow.</p>

<p>- He can fill the medium-sized pail (of size \(Y\)) completely to the top with \(Y\) units of milk and pour it into the size-\(M\) pail, as long as this will not cause the size-\(M\) pail to overflow.</p>

<p>Although FJ realizes he may not be able to completely fill the size-\(M\) pail, please help him determine the maximum amount of milk he can possibly add to this pail.</p>

### 입력 

 <p>The first, and only line of input, contains \(X\), \(Y\), and \(M\), separated by spaces.</p>

### 출력 

 <p>Output the maximum amount of milk FJ can possibly add to the size-\(M\) pail.</p>

