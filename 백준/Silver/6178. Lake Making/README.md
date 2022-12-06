# [Silver IV] Lake Making - 6178 

[문제 링크](https://www.acmicpc.net/problem/6178) 

### 성능 요약

메모리: 115576 KB, 시간: 184 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>Farmer John wants his cows to help him make a lake. He has mapped the pasture where he wants to build the lake by creating a R (3 <= R <= 100) row by C (3 <= C <= 100) column grid of six foot by six foot squares and then by determining the average elevation (10 <= elev_rc <= 5000) in inches for each square.</p>

<p>Additionally, he has trained the cows in "stomp digging". The burly bovines travel in a herd that just exactly covers a 3x3 grid of squares to a grid whose upper left coordinate is R_s,C_s (1 <= R_s <= R-2; 1 <= C_s <= C-2). The cows then stomp the ground to push it down D_s (1 <= D_s <= 40) inches. The cows are quite meticulous; the cows at lower elevations will not commence stomping until the rest of the herd has joined them. Thus, not all the 3x3 grid is necessarily stomped (or perhaps some part is stomped less than some other part).</p>

<p>Given an initial set of elevations, an ordered set of N (1 <= N <= 20000) stomp digging instructions, and an elevation E (0 <= E <= 5000) for the lake's final water level, determine the volume of water (in cubic inches) that the lake will hold. It is guaranteed that the answer will not exceed 2,000,000,000.  Presume that the edge of the lake contains barriers so that water can not spill over the border.</p>

<p>Consider a small 4 x 6 pasture to be turned into a lake. Its initial elevations (annotated with row/column numbers) are:</p>

<pre>                      column
                  1  2  3  4  5  6
         row 1:  28 25 20 32 34 36
         row 2:  27 25 20 20 30 34
         row 3:  24 20 20 20 20 30
         row 4:  20 20 14 14 20 20</pre>

<p>Interpreting the map, we see a hill in the upper right corner that rises to elevation 36; a small hill also rises to elevation 28 in the upper left corner. The middle of row 4 has a slight depression. After the cow-stomping instruction "1 4 4", the pasture has these elevations:</p>

<pre>                  1  2  3  4  5  6
         row 1:  28 25 20 32 32 32
         row 2:  27 25 20 20 30 32
         row 3:  24 20 20 20 20 30
         row 4:  20 20 14 14 20 20</pre>

<p>Note that only three squares were stomped down. The other six sets of cows were waiting for the stompers to get to their level, which never happened.  After stomping down the upper left corner with this instruction "1 1 10", the pasture looks like this:</p>

<pre>                  1  2  3  4  5  6
         row 1:  18 18 18 32 32 32
         row 2:  18 18 18 20 30 32
         row 3:  18 18 18 20 20 30
         row 4:  20 20 14 14 20 20</pre>

<p>If the final elevation of the lake is to be 22 inches, the pasture has these depths:</p>

<pre>                  1  2  3  4  5  6
         row 1:   4  4  4 -- -- --
         row 2:   4  4  4  2 -- --
         row 3:   4  4  4  2  2 --
         row 4:   2  2  8  8  2  2</pre>

<p>for a total aggregated depth of 66. Calculate the volume by multiplying by 6 feet x 6 feet = 66 x 72 inches x 72 inches = 342,144 cubic inches.</p>

<p>Write a program to automate this calculation.</p>

### 입력 

 <ul>
	<li>Line 1: Four space-separated integers: R, C, E, N</li>
	<li>Lines 2..R+1: Line i+1 describes row of squares i with C space-separated integers</li>
	<li>Lines R+2..R+N+1: Line i+R+1 describes stomp-digging instruction i with three integers: R_s, C_s, and D_s</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: A single integer that is the volume of the new lake in cubic inches</li>
</ul>

