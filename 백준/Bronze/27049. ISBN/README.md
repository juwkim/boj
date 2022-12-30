# [Bronze I] ISBN - 27049 

[문제 링크](https://www.acmicpc.net/problem/27049) 

### 성능 요약

메모리: 113112 KB, 시간: 104 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation), 수학(math), 모듈로 곱셈 역원(modular_multiplicative_inverse), 정수론(number_theory)

### 문제 설명

<p>Farmer John's cows enjoy reading books, and FJ has discovered that his cows produce more milk when they read books of a somewhat intellectual nature. He decides to update the barn library to replace all of the cheap romance novels with textbooks on algorithms and mathematics. Unfortunately, a shipment of these new books has fallen in the mud and their ISBN numbers are now hard to read.</p>

<p>An ISBN (International Standard Book Number) is a ten digit code that uniquely identifies a book.  The first nine digits represent the book and the last digit is used to make sure the ISBN is correct.  To verify that an ISBN number is correct, you calculate a sum that is 10 times the first digit plus 9 times the second digit plus 8 times the third digit ... all the way until you add 1 times the last digit.  If the final number leaves no remainder when divided by 11, the code is a valid ISBN.</p>

<p>For example 0201103311 is a valid ISBN, since </p>

<p>10*0 + 9*2 + 8*0 + 7*1 + 6*1 + 5*0 + 4*3 + 3*3 + 2*1 + 1*1 = 55.</p>

<p>Each of the first nine digits can take a value between 0 and 9. Sometimes it is necessary to make the last digit equal to ten; this is done by writing the last digit as X.  For example, 156881111X is a valid ISBN number.</p>

<p>Your task is to fill in the missing digit from a given ISBN number where the missing digit is represented as '?'.</p>

### 입력 

 <ul>
	<li>Line 1: A single line with a ten digit ISBN number that contains '?' in a single  position</li>
</ul>

### 출력 

 <ul>
	<li>Line 1: The missing digit (0..9 or X). Output -1 if there is no acceptable digit  for the position marked '?' that gives a valid ISBN.</li>
</ul>

