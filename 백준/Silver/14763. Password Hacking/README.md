# [Silver III] Password Hacking - 14763 

[문제 링크](https://www.acmicpc.net/problem/14763) 

### 성능 요약

메모리: 108080 KB, 시간: 108 ms

### 분류

정렬

### 제출 일자

2024년 2월 16일 05:40:23

### 문제 설명

<p>We all know that passwords are not very secure unless users are disciplined enough to use passwords that are difficult to guess. But most users are not so careful, and happily use passwords such as “123456”. In fact, there are lists of commonly used passwords that hackers can use for breaking into systems, and these passwords often work.</p>

<p>You have done a lot of hacking using such lists, and you have a good idea of how likely each password in the list is the correct one (you are very surprised by the number of people using “123456” as their passwords). You have a new account to hack, and you have decided to try each of the passwords in the list one at a time, until the correct one is found. You are absolutely sure that the account you want to hack uses a password in the given list.</p>

<p>What is the expected number of attempts to find the correct passwords, assuming that you try these passwords in the optimal order?</p>

### 입력 

 <p>The first line of input contains a positive integer N, the number of passwords in the list. Each of the next N lines gives the password, followed by a space, followed by the probability that the password is the correct one. Each password is a non-empty string consisting only of alphanumeric characters and is up to 12 characters long. Each probability is a real number with 4 decimal places. You may assume that there are at most 500 passwords in the list, and that the sum of all probabilities equals 1. No two passwords in the list are the same.</p>

### 출력 

 <p>Output on a single line the expected number of attempts to find the correct passwords using the optimal order. Answers within 10<sup>−4</sup> of the correct answer will be accepted.</p>

