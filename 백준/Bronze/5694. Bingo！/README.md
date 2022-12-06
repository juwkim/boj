# [Bronze I] Bingo! - 5694 

[문제 링크](https://www.acmicpc.net/problem/5694) 

### 성능 요약

메모리: 118132 KB, 시간: 944 ms

### 분류

구현(implementation), 수학(math)

### 문제 설명

<p>Albert, Charles and Mary invented a new version of the classical game Bingo. In traditional Bingo the game is presided over by a non-player known as the caller. At the beginning of the game each player is given a card containing a unique combination of numbers from 0 to N arranged in columns and rows. The caller has a bag containing N + 1 balls, numbered from 0 to N. On each turn, the caller randomly selects a ball from the bag, announces the number of the drawn ball to the players, and sets the ball aside so that it cannot be selected again. Each player searches his card for the called number and marks it if he finds it. The first player who marks a complete pre-announced pattern on the card (for example, a full horizontal line) wins a prize.</p>

<p>In the Albert-Charles-Mary version, on each turn, the caller draws a first ball, returns it to the bag, draws a second ball, returns it to the bag, and then calls out the absolute difference between the two ball numbers. To generate even more excitement, before the game started a possibly empty subset of balls is removed from the bag, in such a way that at least two balls remain there. They would like to know if every number from 0 to N may still be called out with the new drawing method considering the balls that were left in the bag.</p>

### 입력 

 <p>Each test case is given using exactly two lines. The first line contains two integers N and B. The meaning of N was described above (1 ≤ N ≤ 90), while B represents the number of balls which remained in the bag (2 ≤ B ≤ N + 1). The second line contains B distinct integers b<sub>i</sub>, indicating the balls which remained in the bag (0 ≤ b<sub>i</sub> ≤ N).</p>

<p>The last test case is followed by a line containing two zeros.</p>

### 출력 

 <p>For each test case output a single line containing a single uppercase ‘Y’ if is possible to call out every number from 0 to N, inclusive, or a single uppercase ‘N’ otherwise.</p>

