# [Silver I] Count - 15794 

[문제 링크](https://www.acmicpc.net/problem/15794) 

### 성능 요약

메모리: 189036 KB, 시간: 324 ms

### 분류

이분 탐색, 두 포인터

### 제출 일자

2025년 5월 9일 21:11:39

### 문제 설명

<p>Given is a sequence of n integers: a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>n</sub>. Given is also an integer v. We consider pairs (a<sub>i</sub>, a<sub>j</sub>) of elements from the given sequence, such that i < j. </p>

<p>Write a program count that finds such pair, whose sum a<sub>i</sub> + a<sub>j</sub> is the closest to (or the same as) the value of v and output the number of all such pairs with sums a<sub>i</sub> + a<sub>j</sub> that are equally closest to the value of v.</p>

### 입력 

 <p>On the first line of the standard input, the value of n is written.</p>

<p>On the second line, the values of a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>n</sub>, are written, separated by space.</p>

<p>On the third line, the value of v is written.</p>

### 출력 

 <p>On the standard output, your program has to print one integer, equal to the wanted count of pairs.</p>

