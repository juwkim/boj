# [Silver I] GMO - 9665 

[문제 링크](https://www.acmicpc.net/problem/9665) 

### 성능 요약

메모리: 110876 KB, 시간: 492 ms

### 분류

브루트포스 알고리즘

### 제출 일자

2025년 4월 26일 21:53:22

### 문제 설명

<p>A multinational company is asking you to help them genetically modify an apple. In order for the apples to grow faster, to get more of them, to make them bigger and make them look nicer and more simmetrical, the apple's DNA requires an insertion of a certain swine gene. </p>

<p>The apple's DNA is represented by a series of characters from the set {A, C, G, T}. The required swine gene is also comprised of charaters from this set. The apple's DNA should be injected with some characters into some places, so that the resulting sequence contains a swine gene somewhere (in successive locations). To make things a bit more complicated, inserting each of the characters A, C, G, T has its own cost.</p>

<p>Help this multinational company in achieving their goal with the lowest possible total cost. As a reward, you get a ton of their apples. </p>

### 입력 

 <p>The first line of input contains a sequence of N (1 ≤ N ≤ 10 000) characters which represent the apple's DNA. </p>

<p>The second line of input contains a sequence of M (1 ≤ M ≤ 5 000) characters which represent the swine gene that we want to insert into the apple's DNA. </p>

<p>Both the sequences are comprised only of characters from the set {A, C, G, T}. </p>

<p>The third line of input contains four integers from the interval [0, 1000]: the cost of inserting one character A, C, G, T, in that order. </p>

### 출력 

 <p>The first and only line of output must contains the minimal total cost. </p>

