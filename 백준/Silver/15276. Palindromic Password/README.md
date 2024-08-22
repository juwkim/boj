# [Silver III] Palindromic Password - 15276 

[문제 링크](https://www.acmicpc.net/problem/15276) 

### 성능 요약

메모리: 110424 KB, 시간: 108 ms

### 분류

브루트포스 알고리즘

### 제출 일자

2024년 8월 23일 04:07:05

### 문제 설명

<p>The IT department at your school decided to change their password policy. Each password will have to consist of N 6-digit numbers separated by dashes, where N will be determined by the phase of the moon and the weather forecast for the day after it will be generated.</p>

<p>You realized that, if all of the numbers were palindromes (same numbers as the original ones if read backwards), you would have to remember a bunch of 3-digit numbers, which did not sound that bad (at the time).</p>

<p>In order to generate your password of N numbers, you get a list of N randomly generated 6-digit numbers and find the palindromic number closest to them.</p>

<p>Of course, you would like to automate this process...</p>

### 입력 

 <p>The first line of the input contains a single positive integer N ≤ 1000 indicating the number of six-digit numbers in the input. Each of the next N lines contains a six-digit number without leading zeroes.</p>

### 출력 

 <p>For each six-digit number in the input, output another six-digit number that is closest to it and is also a palindrome. “Closest” in this context means “a number having the smallest absolute difference with the original number”. If there are two different numbers satisfying the above condition, output the smaller one of the two. Remember, no leading zeroes.</p>

