# [Bronze II] Knot Knowledge - 23275 

[문제 링크](https://www.acmicpc.net/problem/23275) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

구현(implementation)

### 문제 설명

<p>Sonja the scout is taking a test to see if she knows all the knots a scout is supposed to know.  The Scout's Big Book of Knots has descriptions of $1\,000$ different knots, conveniently numbered from $1$ to $1\,000$.  For the test, Sonja needs to learn a specific set of $n$ of these knots.  After some intense studying, she has learned all except one of them, but she has forgotten which knot she does not yet know.</p>

<p>Given the list of knots Sonja needs to learn, and the ones she has learned so far, find the remaining knot to learn.</p>

### 입력 

 <p>The first line of input consists of an integer $n$ ($2 \le n \le 50$), the number of knots Sonja needs to learn. This is followed by a line containing $n$ distinct integers $x_1, \ldots, x_n$ ($1 \le x_i \le 1\,000$), the knots that Sonja needs to learn. Finally, the last line contains $n-1$ distinct integers $y_1, \ldots, y_{n-1}$ ($1 \le y_i \le 1\,000$), the knots that Sonja has learned so far.  You may assume that each knot Sonja has learned is one of the $n$ knots she was supposed to learn.</p>

### 출력 

 <p>Output the number of the remaining knot that Sonja needs to learn.</p>

