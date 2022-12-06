# [Bronze III] Baskets of Gold Coins - 4850 

[문제 링크](https://www.acmicpc.net/problem/4850) 

### 성능 요약

메모리: 30840 KB, 시간: 248 ms

### 분류

사칙연산(arithmetic), 수학(math)

### 문제 설명

<p>You are given N baskets of gold coins. The baskets are numbered from 1 to N. In all except one of the baskets, each gold coin weighs w grams. In the one exceptional basket, each gold coin weighs w−d grams. A wizard appears on the scene and takes 1 coin from Basket 1, 2 coins from Basket 2, and so on, up to and including N−1 coins from Basket N−1. He does not take any coins from Basket N. He weighs the selected coins and concludes which of the N baskets contains the lighter coins. Your mission is to emulate the wizard's computation.</p>

### 입력 

 <p>The input file will consist of one or more lines; each line will contain data for one instance of the problem. More specifically, each line will contain four positive integers, separated by one blank space. The first three integers are, respectively, the numbers N, w, and d, as described above. The fourth integer is the result of weighing the selected coins.</p>

<p>N will be at least 2 and not more than 8000. The value of w will be at most 30. The value of d will be less than w.</p>

### 출력 

 <p>For each instance of the problem, your program will produce one line of output, consisting of one positive integer: the number of the basket that contains lighter coins than the other baskets.</p>

