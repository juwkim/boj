# [Bronze II] A Game with Marbles - 6508 

[문제 링크](https://www.acmicpc.net/problem/6508) 

### 성능 요약

메모리: 28776 KB, 시간: 72 ms

### 분류

구현(implementation), 수학(math), 시뮬레이션(simulation)

### 문제 설명

<p>There are <em>n</em> bowls, numbered from <em>1</em> to <em>n</em>. Initially, bowl <em>i</em> contains <em>m<sub>i</sub></em> marbles. One game step consists of removing one marble from a bowl. When removing a marble from bowl <em>i</em> (<em>i > 1</em>), one marble is added to each of the first <em>i-1</em> bowls; if a marble is removed from bowl <em>1</em>, no new marble is added. The game is finished after each bowl is empty.</p>

<p>Your job is to determine how many game steps are needed to finish the game. You may assume that the supply of marbles is sufficient, and each bowl is large enough, so that each possible game step can be executed.</p>

### 입력 

 <p>The input contains several test cases. Each test case consists of one line containing one integer <em>n</em> (<em>1 ≤ n ≤ 50</em>), the number of bowls in the game. The following line contains <em>n</em> integers <em>m<sub>i</sub></em> (<em>1 ≤ i ≤ n, 0 ≤ m<sub>i</sub> ≤ 1000</em>), where <em>m<sub>i</sub></em> gives the number of marbles in bowl <em>i</em> at the beginning of the game.</p>

<p>The last test case is followed by a line containing <em>0</em>.</p>

### 출력 

 <p>For each test case, print one line with the number of game steps needed to finish the game. You may assume that this number fits into a signed 64-bit integer (in C/C++ you can use the data type "long long", in JAVA the data type "long").</p>

