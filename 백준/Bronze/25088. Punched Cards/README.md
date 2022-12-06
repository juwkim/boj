# [Bronze II] Punched Cards - 25088 

[문제 링크](https://www.acmicpc.net/problem/25088) 

### 성능 요약

메모리: 30840 KB, 시간: 84 ms

### 분류

구현(implementation)

### 문제 설명

<p>A secret team of programmers is plotting to disrupt the programming language landscape and bring punched cards back by introducing a new language called <i>Punched Card Python</i> that lets people code in Python using punched cards! Like good disrupters, they are going to launch a viral campaign to promote their new language before even having the design for a prototype. For the campaign, they want to draw punched cards of different sizes in ASCII art.</p>

<p style="text-align: center;"><img alt="" src="" style="width: 558px; height: 250px;"></p>

<p>The ASCII art of a punched card they want to draw is similar to an $R×C$ matrix without the top-left cell. That means, it has $(R⋅C)-1$ cells in total. Each cell is drawn in ASCII art as a period (<code>.</code>) surrounded by dashes (<code>-</code>) above and below, pipes (<code>|</code>) to the left and right, and plus signs (<code>+</code>) for each corner. Adjacent cells share the common characters in the border. Periods (<code>.</code>) are used to align the cells in the top row.</p>

<p>For example, the following is a punched card with $R=3$ rows and $C=4$ columns:</p>

<pre align="center">..+-+-+-+
..|.|.|.|
+-+-+-+-+
|.|.|.|.|
+-+-+-+-+
|.|.|.|.|
+-+-+-+-+
</pre>

<p>There are more examples with other sizes in the samples below. Given the integers $R$ and $C$ describing the size of a punched card, print the ASCII art drawing of it as described above.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, $T$. $T$ lines follow, each describing a different test case with two integers $R$ and $C$: the number of rows and columns of the punched card that must be drawn.</p>

### 출력 

 <p>For each test case, output one line containing <code>Case #x:</code>, where $x$ is the test case number (starting from 1). Then, output $(2⋅R)+1$ additional lines with the ASCII art drawing of a punched card with $R$ rows and $C$ columns.</p>

