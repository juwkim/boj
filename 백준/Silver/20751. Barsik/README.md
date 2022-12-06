# [Silver V] Barsik - 20751 

[문제 링크](https://www.acmicpc.net/problem/20751) 

### 성능 요약

메모리: 116312 KB, 시간: 304 ms

### 분류

애드 혹(ad_hoc), 구현(implementation), 수학(math)

### 문제 설명

<p>In one of the corners of a $N$ $\times$ $M$-sized rectangular field, in a cell with the coordinates ($1$, $1$), sits a hungry cat named Barsik. Barsik's bowl is in the opposite corner of the field, in the cell with the coordinates ($N$, $M$). Barsik can traverse the field by moving between cells adjacent by side.</p>

<p>However, there is an obstacle, a vicious dog named Tuzik, who sits in a kennel with the coordinates ($R$, $C$). Tuzik is chained to the kennel and thus can only reach cells that are within $S$ moves from the kennel (each move going to a cell adjacent by side). All such cells are filled with bones of dead barsiks, and our Barsik cannot make himself walk through them.</p>

<p>Barsik desperately needs to know if he can reach his bowl without stepping into Tuzik's area.</p>

### 입력 

 <p>The first line of the input file contains an integer $T$ --- the number of tests in the problem ($1 \le T \le 2\,000$).</p>

<p>The following $T$ lines contain descriptions of tests, one per line.</p>

<p>Each tests consists of five space-separated integers $N$, $M$, $R$, $C$, and $S$ ($1 \le R \le N \le 10^9$, $1 \le C \le M \le 10^9$, $1 \le S \le 10^9$).</p>

<p>It is guaranteed that the cell with Tuzik's kennel is placed in such a manner that he cannot reach neither the cell with the original position of Barsik nor the cell with Barsik's food.</p>

### 출력 

 <p>For each test, print an answer in a separate line. Print <code>Barsik</code>, if Barsik can reach the food without stepping over bones. Otherwise print <code>Tuzik</code>.</p>

