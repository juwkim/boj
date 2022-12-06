# [Bronze II] Magnificent Meatballs - 4646 

[문제 링크](https://www.acmicpc.net/problem/4646) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

구현(implementation), 수학(math)

### 문제 설명

<p>Sam and Ella run a catering service. They like to put on a show when serving meatballs to guests seated at round tables. They march out of the kitchen with pots of meatballs and start serving adjacent guests. Ella goes counterclockwise and Sam goes clockwise, until they both plop down their last meatball, at the same time, again at adjacent guests. This impressive routine can only be accomplished if they can divide the table into two sections, each having the same number of meatballs. You are to write a program to assist them.</p>

<p>At these catering events, each table seats 2 <= N <= 30 guests. Each guest orders at least one and at most nine meatballs. Each place at the table is numbered from 1 to N, with the host at position 1 and the host's spouse at position N. Sam always serves the host first then proceeds to serve guests in increasing order. Ella serves the spouse first, then serves guests in decreasing order. The figures illustrate the first two example input cases.</p>

<p style="text-align:center"><img alt="" src="" style="height:208px; width:447px"></p>

### 입력 

 <p>Input consists of one or more test cases. Each test case contains the number of guests N followed by meatballs ordered by each guest, from guest 1 to guest N. The end of the input is a line with a single zero.</p>

### 출력 

 <p>For each table, output a single line with the ending positions for Sam and Ella, or the sentence indicating an equal partitioning isn't possible. Use the exact formatting shown below.</p>

