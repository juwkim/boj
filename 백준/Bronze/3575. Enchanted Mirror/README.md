# [Bronze II] Enchanted Mirror - 3575 

[문제 링크](https://www.acmicpc.net/problem/3575) 

### 성능 요약

메모리: 113112 KB, 시간: 116 ms

### 분류

자료 구조, 문자열

### 문제 설명

<p>Alice likes two things in this world — her mirror and her toy bricks. Alice’s toy bricks were designed to help the children to learn the alphabet, so there are some letters written on their top faces. Alice likes to play with the bricks near the mirror.</p>

<p>When Alice learned the alphabet, she noticed that something was wrong with her mirror! A brick in the mirror can show a different letter on it. Alice enjoyed this thing very much, and she invented a new game, trying to make some funny words from the bricks in the real world and in the mirror simultaneously.</p>

<p>The rules of this game are the following. Alice creates a line from some bricks that shows the word S<sub>1</sub>. This line is shown in the mirror as some word S<sub>2</sub>, which may be different from the reflection of S<sub>1</sub> because the mirror is enchanted. But the length of each of these words is equal to the same integer number N.</p>

<p>Then Alice can repeat the following step. She selects some two bricks i and j and swaps them. The reflected Alice in the mirror does exactly the same with the mirrored line, except that she of course swaps the bricks with positions N − i + 1 and N − j + 1 in it.</p>

<p>The goal is to create word T<sub>1</sub> in the real world simultaneously with the word T<sub>2</sub> in the mirror. Alice wonders whether it is possible and she asks you for help. Write a program which can determine whether the goal can be achieved.</p>

### 입력 

 <p>The input file contains four words S<sub>1</sub>, S<sub>2</sub>, T<sub>1</sub> and T<sub>2</sub>, in this order, each on the separate line. All words have the same length N (1 ≤ N ≤ 100) and consist only of uppercase English letters.</p>

### 출력 

 <p>If the goal can be achieved, output “Yes”. Otherwise output “No”.</p>

