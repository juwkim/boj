# [Silver III] Ready for Contest - 32316 

[문제 링크](https://www.acmicpc.net/problem/32316) 

### 성능 요약

메모리: 139300 KB, 시간: 284 ms

### 분류

자료 구조, 해시를 사용한 집합과 맵, 구현, 정렬

### 제출 일자

2024년 9월 17일 17:56:37

### 문제 설명

<p>Whenever the UCF Programming Team Coaches prepare for the UCF Local Programming Contest, each problem requires valid judge solutions in C++ and Java. Python solutions may be written as well, but these are optional. Thus, the coaches consider a problem to be ready for the contest if it has at least one C++ solution and at least one Java solution.</p>

<p>Unfortunately, instead of writing solutions for the problems that need them, the coaches just pick their favorite problems and write solutions for those instead. Naturally, they use their favorite language as well instead of checking to see what solutions hasn't been written yet.</p>

<p>Although many solutions have been written, it may be the case that some problems aren't ready for the contest yet. Write a program to determine which problems are ready to go!</p>

<p>Given the number of problems that have been proposed, and a list of every solution written (which problem and which language), determine the problems that are contest ready (have both a C++ and a Java solution written).</p>

### 입력 

 <p>The first input line contains two integers: n (1 ≤ n ≤ 10<sup>5</sup>), indicating the number of problems proposed and m (2 ≤ m ≤ 3×10<sup>5</sup>), indicating the number of solutions written. The problems are numbered 1 through n.</p>

<p>The information about each solution written are provided in the following m input lines, with each line specifying a single solution written. Each of these input lines contains two integers: p (1 ≤ p ≤ n), and L (1 ≤ L ≤ 3), indicating that a solution has been written for problem number p in language L. If L = 1, the language is C++; if L = 2, the language is Java; if L = 3, the language is Python.</p>

### 출력 

 <p>Print a list of the problems that are ready for contest, sorted in numerical order, with one number outputted per line. It is guaranteed that at least one problem will be ready for contest so there will be some output.</p>

