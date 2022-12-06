# [Silver V] The Amazing Human Cannonball - 24775 

[문제 링크](https://www.acmicpc.net/problem/24775) 

### 성능 요약

메모리: 32952 KB, 시간: 76 ms

### 분류

기하학(geometry), 수학(math), 물리학(physics)

### 문제 설명

<p><img alt="" src="" style="width: 400px; height: 225px; float: right;">The amazing human cannonball show is coming to town, and you are asked to double-check their calculations to make sure no one gets injured! The human cannonball is fired from a cannon that is a distance $x_1$ from a vertical wall with a hole through which the cannonball must fly.  The lower edge of the hole is at height $h_1$ and the upper edge is at height $h_2$.  The initial velocity of the cannonball is given as $v_0$ and you also know the angle $\theta$ of the cannon relative to the ground.</p>

<p>Thanks to their innovative suits, human cannonballs can fly without air resistance, and thus their trajectory can be modeled using the following formulas: \begin{eqnarray*} x(t) & = & v_0 t \cos{\theta} \\ y(t) & = & v_0 t \sin{\theta} - \frac{1}{2} g t^2 \end{eqnarray*} where $x(t), y(t)$ provides the position of a cannon ball at time $t$ that is fired from point $(0, 0)$. $g$ is the acceleration due to gravity ($g = 9.81\ m/s^2$).</p>

<p>Write a program to determine if the human cannonball can make it safely through the hole in the wall.  To pass safely, there has to be a vertical safety margin of $1m$ both below and above the point where the ball's trajectory crosses the centerline of the wall.</p>

### 입력 

 <p>The input will consist of up to $100$ test cases.  The first line contains an integer $N$, denoting the number of test cases that follow. Each test case has 5 parameters: $v_0 \ \theta \ x_1 \ h_1 \ h_2$, separated by spaces. $v_0$ ($0 < v_0 \le 200$) represents the ball's initial velocity in $m/s$. $\theta$ is an angle given in degrees ($0 < \theta < 90$), $x_1$ ($0 < x_1 < 1000$) is the distance from the cannon to the wall, $h_1$ and $h_2$ ($0 < h_1 < h_2 < 1000$) are the heights of the lower and upper edges of the wall. All numbers are floating point numbers.</p>

### 출력 

 <p>If the cannon ball can safely make it through the wall, output "<code>Safe</code>".  Otherwise, output "<code>Not Safe</code>"!</p>

