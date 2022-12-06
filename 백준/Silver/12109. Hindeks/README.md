# [Silver V] Hindeks - 12109 

[문제 링크](https://www.acmicpc.net/problem/12109) 

### 성능 요약

메모리: 199248 KB, 시간: 320 ms

### 분류

구현(implementation), 정렬(sorting)

### 문제 설명

<p>How do we evaluate the success of a scientist? By the number of published papers or by their impact - more precisely, the number of citations? Both elements matter. We say that a scientific paper has a citation score C if other scientists cited the paper in question in their paper (referred to it) a total of C times. One of the possible metrics of the success of scientists is their h-index that takes into account both the amount of papers and their citation scores.</p>

<p>A scientist’s h-index is defined as the largest number H with the following properties: the scientist can choose H papers such that their citation score is at least H. For example, if a scientist wrote 10 papers such that each of them has been cited 10 or more times, their h-index is (at least) 10.</p>

<p>Write a programme that inputs the citation scores of all papers of a given scientist and outputs their h-index.</p>

### 입력 

 <p>The first line of input contains the positive integer N (1 ≤ N ≤ 500 000), the number of papers of a given scientist.</p>

<p>The following line contains N non-negative integers from the interval [0, 1 000 000], the citation scores of the respective papers.</p>

### 출력 

 <p>The first and only line of output must contain the required h-index.</p>

