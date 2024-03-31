# [Silver III] Vote-Value Disparity 2 - 21830 

[문제 링크](https://www.acmicpc.net/problem/21830) 

### 성능 요약

메모리: 4528 KB, 시간: 0 ms

### 분류

애드 혹, 해 구성하기, 휴리스틱

### 제출 일자

2024년 4월 1일 08:27:03

### 문제 설명

<p>A national election will be held in the JOI kingdom. The JOI kingdom consists of N provinces.</p>

<p>The map of the JOI kingdom is a rectangular-shaped grid consisting of H ×W blocks. There are H blocks in the vertical direction, and there are W blocks in the horizontal direction. A block is connected with another block by one of the four sides (left, right, top, bottom) of it. The H × W blocks are divided into N provinces. Each province is a connected region consisting of blocks. In total, there are P<sub>i</sub> voters in the i-th province (1 ≤ i ≤ N).</p>

<p>You are the chairman of the National Election Committee of JOI. Your task is to divide the N provinces into K electoral districts (1 ≤ K ≤ N) in order to elect K representatives. Each electoral district should contain at least one province, and the blocks belonging to an electoral district should form a connected region. Note that a block is connected with another block by one of the four sides (left, right, top, bottom). Two blocks sharing only a vertex are not connected.</p>

<p>For each electoral district, the ratio 1/(the number of voters in the electoral district) is called the <strong>weight of a single vote</strong> of the electoral district. <strong>The vote-value disparity</strong> is defined to be the maximal weight of a single vote for all electoral districts divided by the the minimal weight of a single vote for all electoral districts.</p>

<p>Recently, the value of “the vote-value disparity” becomes a serious social issue. You have to make this value as small as possible.</p>

<p>Given the information of the provinces of the JOI kingdom and the number of representatives, determine how to divide the provinces into electoral districts so that the value of the vote-value disparity is as small as possible.</p>

### 입력 

 <p>Read the following data from the standard input.</p>

<ul>
	<li>The first line of input contains four space separated integers H, W, N, K, where the height of the map of the JOI kingdom is H, the width is W, the number of provinces is N, the number of representatives is K.</li>
	<li>Each of the following H lines contains W space separated integers. In the i-th line (1 ≤ i ≤ H), the j-th integer (j ≤ j ≤ W) is S<sub>ij</sub> (1 ≤ S<sub>ij</sub> ≤ N). This means the block in i-th row from above and the j-th column from left belongs to the S<sub>ij</sub>-th province.</li>
	<li>In the i-th line (1 ≤ i ≤ N) of the following N lines contains an integer P<sub>i</sub>, the number of voters in the i-th province.</li>
</ul>

### 출력 

 <p>Write the way to divide the provinces into electoral districts in N lines. The i-th line (1 ≤ i ≤ N) of output should contain an integer, the number of the electoral district where the i-th province belongs.</p>

