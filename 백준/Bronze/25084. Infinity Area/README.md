# [Bronze III] Infinity Area - 25084 

[문제 링크](https://www.acmicpc.net/problem/25084) 

### 성능 요약

메모리: 30840 KB, 시간: 76 ms

### 분류

기하학(geometry), 구현(implementation), 수학(math)

### 문제 설명

<p>Let us assume for the simplicity of this problem that the Infinity symbol is made of circles which touch externally at point $S$ as shown below, and let us call it the center of the infinity.</p>

<p>You are given three integers $R$, $A$, $B$. You are currently at the center of the infinity. You will first start drawing the right circle with radius $R$ and reach again the center of infinity. After that, you start drawing the left circle with the radius equal to the radius of last circle multiplied by $A$. After reaching the center of the infinity you again start drawing the right circle with radius equal to the radius of last circle divided by $B$ (<a href="https://mathworld.wolfram.com/IntegerDivision.html" target="_blank">integer divison</a>). After reaching the center of infinity you again draw the left circle with the radius equal to the radius of last circle multiplied by $A$.</p>

<p style="text-align: center;"><img alt="" src="" style="width: 512px; height: 288px;"></p>

<p>You continue to draw the left and right circles as described above until the radius of the circle to be drawn becomes zero. Calculate the sum of areas of all the circles drawn. It is guaranteed that the process will terminate after finite number of steps.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, $T$. $T$ lines follow.</p>

<p>Each line represents a test case and contains three integers $R$, $A$, $B$, where $R$ denotes the radius of the first circle, and $A$ and $B$ are the parameters used to calculate the radii of the subsequent circles.</p>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where $x$ is the test case number (starting from 1) and $y$ is the sum of areas of all the circles drawn until radius of the circle to be drawn becomes zero.</p>

<p>$y$ will be considered correct if it is within an absolute or relative error of $10^{-6}$ of the correct answer.</p>

