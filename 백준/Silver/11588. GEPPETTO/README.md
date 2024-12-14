# [Silver II] GEPPETTO - 11588 

[문제 링크](https://www.acmicpc.net/problem/11588) 

### 성능 요약

메모리: 112956 KB, 시간: 316 ms

### 분류

비트 집합, 브루트포스 알고리즘

### 제출 일자

2024년 12월 15일 07:06:47

### 문제 설명

<p>Everyone’s favorite character and puppet-maker Geppetto has opened a new pizza place, the best in town. Geppetto is trying to make the best pizza possible, but at the same time he doesn’t want to have a small selection of pizzas.</p>

<p>He makes his pizzas out of N ingredients marked with numbers from 1 to N. All that would be simple if he could mix any ingredient with every ingredient on the pizza, but unfortunately, that is not the case. Sometimes some ingredients cannot mix and that creates additional complications for our pizza master.</p>

<p>There are M pairs of ingredients that cannot be on the same pizza at the same time. Given these restrictions, Geppetto wants to know how many different pizzas he can make. Help him answer this question. Two pizzas are considered different if there is an ingredient of index i that is on one pizza, but not on the other.</p>

### 입력 

 <p>The first line of input contains two integers N and M (1 ≤ N ≤ 20, 1 ≤ M ≤ 400). Each of the following M lines contains two different numbers a i b, they represent the prohibition of mixing ingredients marked with a and b on the pizza. (1 ≤ a, b ≤ N). All pairs of ingredients are not necessarily distinct, some pair could occur multiple times.</p>

### 출력 

 <p>The first and only line of output must contain the number of different pizzas given the restrictions in the task.</p>

