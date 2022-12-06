# [Silver V] Triangles - 8117 

[문제 링크](https://www.acmicpc.net/problem/8117) 

### 성능 요약

메모리: 129820 KB, 시간: 296 ms

### 분류

브루트포스 알고리즘(bruteforcing), 기하학(geometry), 그리디 알고리즘(greedy), 정렬(sorting)

### 문제 설명

<p>In a finite sequence of positive integers not greater than a billion, representing lengths of line segments, we want to find three numbers such that one can build a triangle from segments of such lengths.</p>

<p>Write a program which examines whether among the line segments - lengths of which are written in the standard input - there exist three such that one can build a triangle from them. If so, the program writes the lengths of those three segments in the standard output. If there exist no such triple, the program writes one word <code>NIE</code> ("<i>no</i>") in the file standard output.</p>

<p>If there exist many triples of line segments of lengths written in the standard input such that one can build a triangle from them, then your program should find and write only one (arbitrary) of them.</p>

### 입력 

 <p>In the standard input there is a finite sequence of at least three positive integers not greater then 1,000,000,000, terminated by the number 0. Each number is written in a separate line. Positive numbers are lengths of line segments, and the number 0 denotes the end of the data.</p>

<p>The data in the standard input are written correctly and your program need not verify that.</p>

### 출력 

 <p>In the standard output there should be either one word <code>NIE</code>, or three lengths of line segments chosen from the standard input, from which one can build a triangle. The lengths are separated by single spaces.</p>

