# [Silver V] Painting roofs - 23428 

[문제 링크](https://www.acmicpc.net/problem/23428) 

### 성능 요약

메모리: 115152 KB, 시간: 160 ms

### 분류

브루트포스 알고리즘(bruteforcing)

### 문제 설명

<p>The King of Berland loves order in everything. For instance, the capital of Berland as seen on the map is a rectangular field of cells, that correspond to city quarters.     </p>

<p>He recently has issued a decree stating that all roofs in a quarter must be painted the same color --- either red or blue. The capital of Berland is expecting a commission which will check the whole city for compliance, moving from one quarter to an adjacent by a side quarter. For a successful check, the commission must be able to reach any quarter from any other.</p>

<p>The Minister of Finance found out that the commission has a curious demand. They cannot move to an adjacent quarter if its roofs have the same color as roofs of the quarter they are currently in. Consequently, some quarters will have to repaint all their roofs to pass the check. The Minister of Finance wants to save money. He's asking you to find the minimal number of quarters where all roofs must be repainted.</p>

### 입력 

 <p>The first line of the input file contains two integers $m$ and $n$ --- the number of lines and columns in the city map ($1\le m, n\le 1000$). Next come $m$ lines consisting of $n$ symbols, with each symbol being either '1', or '2'. The symbol '1' means that all roofs in the corresponding quarters are blue, and the symbol '2' means that the roofs are red.</p>

### 출력 

 <p>In the output file, print a single integer --- the minimal number of quarters where roofs must be repainted.</p>

