# [Silver IV] Need For Speed - 6039 

[문제 링크](https://www.acmicpc.net/problem/6039) 

### 성능 요약

메모리: 116060 KB, 시간: 168 ms

### 분류

비트마스킹(bitmask), 브루트포스 알고리즘(bruteforcing)

### 문제 설명

<p>Bessie is preparing her race car for the upcoming Grand Prix, but she wants to buy some extra parts to improve the car's performance. Her race car currently has mass M (1 <= M <= 1,000) and is able to push itself forward with a force of F (1 <= F <= 1,000,000). The Race Car Performance Store has N (1 <= N <= 20) parts conveniently numbered 1..N. Bessie can buy as many or as few parts as she wishes though the store stocks no more than one instance of each part.</p>

<p>Part P_i adds force F_i (1 <= F_i <= 1,000,000) and has mass M_i (1 <= M_i <= 1,000). Newton's Second Law decrees that F = MA, where F is force, M is mass, and A is acceleration. If Bessie wants to maximize the total acceleration of her race car (and minimize the mass otherwise), which extra parts should she choose?</p>

<p>Consider a race car with initial F=1500 and M=100. Four parts are available for enhancement:</p>

<pre>          i  F_i  M_i
          1  250   25
          2  150    9
          3  120    5
          4  200    8</pre>

<p>Adding just part 2, e.g., would result in an acceleration of (1500+150)/(100+9) = 1650/109 = 15.13761.</p>

<p>Below is a chart of showing the acceleration for all possible combinations of adding/not-adding the four parts (in column one, 1=part added, 0=part not added):</p>

<pre>Parts   Aggregate   Aggregate        
1234        F           M       F/M
0000      1500         100    15.0000
0001      1700         108    15.7407
0010      1620         105    15.4286
0011      1820         113    16.1062
0100      1650         109    15.1376
0101      1850         117    15.8120
0110      1770         114    15.5263
0111      1970         122    16.1475 <-- highest F/M
1000      1750         125    14.0000
1001      1950         133    14.6617
1010      1870         130    14.3846
1011      2070         138    15.0000
1100      1900         134    14.1791
1101      2100         142    14.7887
1110      2020         139    14.5324
1111      2220         147    15.1020</pre>

<p>Thus, the best additional part combination is parts 2, 3, and 4.</p>

### 입력 

 <ul>
	<li>Line 1: Three space-separated integers: F, M, and N</li>
	<li>Lines 2..N+1: Line i+1 contains two space separated integers: F_i and M_i</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Lines 1..P: The index values of P extra parts, one per line, that Bessie should add to her racecar. If she should not add any, output 'NONE' (without quotes). The output should be given in increasing order, so if the optimal set of parts is {2,4,6,7}, then the output should be in the order 2,4,6,7 and not, for example, 4,2,7,6.</li>
</ul>

<p> </p>

