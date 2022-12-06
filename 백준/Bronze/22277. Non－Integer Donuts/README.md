# [Bronze I] Non-Integer Donuts - 22277 

[문제 링크](https://www.acmicpc.net/problem/22277) 

### 성능 요약

메모리: 30840 KB, 시간: 108 ms

### 분류

수학(math), 파싱(parsing), 문자열(string)

### 문제 설명

<p>Neil is a very important lawyer with a very important bank account. Since Neil is such a successful lawyer with many clients, he deposits money to his account every single morning.</p>

<p>After going to the bank and depositing money, Neil goes to work. And there lies Neil’s great weakness: a donut shop. You see, Neil is a recovering donut addict, and although he hasn’t eaten a donut in years, he can’t help but wonder how many \$1.00 donuts he could buy with the money in his account if he were to relapse.</p>

<p>Having \$5.00 in his account means 5 donuts Neil could have, but what about \$4.50? Well, that is more than 4 donuts for sure, but definitely less than 5. How would one even buy a non-integer amount of donuts? That concept confuses Neil, so every time his account balance is not an integer, he stops to ponder the nature of non-integer donuts and ends up being late to work.</p>

<p>Now Neil has been late too many times and is starting to worry he will lose his job. He wants to know how many times he will be late to work during the next N days, given his initial account balance and the amount of money he will deposit each day. Please answer this for him, or else Neil will start pondering again.</p>

### 입력 

 <p>The first line contains an integer N (1 ≤ N ≤ 1000), the number of days Neil is interested in. Each of the next N + 1 lines contains a string representing an amount of money. The first string is Neil’s account initial balance, while the following N strings are the amounts Neil will deposit to his account in the different days. Each string has the form \$X.Y where X is a substring of length 1 or 2 indicating the whole money in the amount \$X.Y, while Y is a substring of length exactly 2 denoting the cents in the amount \$X.Y. Both X and Y are made of digits, at least one of them contains a non-zero digit, and X does not have leading zeros.</p>

### 출력 

 <p>Output a single line with an integer indicating how many times Neil will be late to work during the following N days.</p>

