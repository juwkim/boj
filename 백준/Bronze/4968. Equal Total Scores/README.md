# [Bronze I] Equal Total Scores - 4968 

[문제 링크](https://www.acmicpc.net/problem/4968) 

### 성능 요약

메모리: 30840 KB, 시간: 112 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation), 수학(math)

### 문제 설명

<p>Taro and Hanako have numbers of cards in their hands. Each of the cards has a score on it. Taro and Hanako wish to make the total scores of their cards equal by exchanging one card in one's hand with one card in the other's hand. Which of the cards should be exchanged with which?</p>

<p>Note that they have to exchange their cards even if they already have cards of the same total score.</p>

### 입력 

 <p>The input consists of a number of datasets. Each dataset is formatted as follows.</p>

<pre>n m
s<sub>1</sub>
s<sub>2</sub>
...
s<sub>n</sub>
s<sub>n+1</sub>
s<sub>n+2</sub>
...
s<sub>n+m</sub></pre>

<p>The first line of a dataset contains two numbers n and m delimited by a space, where n is the number of cards that Taro has and m is the number of cards that Hanako has. The subsequent n+m lines list the score for each of the cards, one score per line. The first n scores (from s<sub>1</sub> up to s<sub>n</sub>) are the scores of Taro's cards and the remaining m scores (from s<sub>n+1</sub> up to s<sub>n+m</sub>) are Hanako's.</p>

<p>The numbers n and m are positive integers no greater than 100. Each score is a non-negative integer no greater than 100.</p>

<p>The end of the input is indicated by a line containing two zeros delimited by a single space.</p>

### 출력 

 <p>For each dataset, output a single line containing two numbers delimited by a single space, where the first number is the score of the card Taro gives to Hanako and the second number is the score of the card Hanako gives to Taro. If there is more than one way to exchange a pair of cards that makes the total scores equal, output a pair of scores whose sum is the smallest.</p>

<p>In case no exchange can make the total scores equal, output a single line containing solely -1. The output must not contain any superfluous characters that do not conform to the format.</p>

