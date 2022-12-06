# [Bronze I] Extending Rock-Paper-Scissors - 16104 

[문제 링크](https://www.acmicpc.net/problem/16104) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

구성적(constructive)

### 문제 설명

<p>Rock-paper-scissors is a game played between two players, where each player chooses one of three elements: rock, paper or scissors. The rules are simple: rock-beats-scissors, scissors-beats-paper and paper-beats-rock. If the players choose the same element, then they tie. On the television show The Big Bang Theory, Sheldon extended rock-paper-scissors to include two extra elements: Lizard and Spock.</p>

<p>The rules are scissors-cuts-paper, paper-covers-rock, rock-crushes-lizard, lizard-poisons-Spock, Spock-smashes-scissors, scissors-decapitates-lizard, lizard-eats-paper, paper-disproves-Spock, Spock-vaporizes-rock and rock-crushes-scissors.</p>

<p>Sheldon’s setup is valid since each element beats exactly half of the other elements and loses to the remaining half. Whenever the number of elements is odd, it is possible to find a game that satisfies these criteria. Extend the game to n elements.</p>

### 입력 

 <p>The input consists of a single line with one integer n (3 ≤ n ≤ 99), which is the number of elements. It is guaranteed that n is odd.</p>

### 출력 

 <p>Display one valid extension of rock-paper-scissors to n elements. Display exactly n(n−1)/2 lines containing two integers each, b and c (b ≠ c), indicating that element b beats element c. The elements are numbered 1, 2, . . . , n.</p>

<p>For each pair of distinct elements, x and y, exactly one of ‘x y’ or ‘y x’ should be displayed. The lines may be displayed in any order. If there are multiple solutions, any one will be accepted.</p>

