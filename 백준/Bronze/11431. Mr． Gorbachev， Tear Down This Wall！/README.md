# [Bronze II] Mr. Gorbachev, Tear Down This Wall! - 11431 

[문제 링크](https://www.acmicpc.net/problem/11431) 

### 성능 요약

메모리: 30840 KB, 시간: 440 ms

### 분류

구현(implementation)

### 문제 설명

<p>One of the iconic moments of the reunification between Eastern and Western Germany was when the wall separating East and West Berlin was torn down. Pieces of brick from the wall are now part of many museums and private collections.<sup>1</sup> Famously, in 1987, President Reagan had asked the Soviet Union to allow East Germany to open up to the West with the now-famous phrase “Mr. Gorbachev, Tear Down This Wall!” Of course, it would have taken Mr. Gorbachev himself quite a while to do so, since the wall was quite long and sturdy. So he’d likely have asked a few buddies to help. Here, you are to compute how long it would have taken them together to tear down the Berlin wall.</p>

<p>You will be given a description of the wall as a sequence of points in a 2-D coordinate system; all coordinates will be integers, and we will make sure that all wall pieces are either horizontal or vertical, but never at an angle. You will also be told how much wall (length) per hour one person can tear down, and how many people there are. From this, you are to compute the necessary time to tear down the wall.</p>

<p><sup>1</sup>As are, most likely, random pieces of brick sold for a fortune to tourists who were not able to tell whether a particular piece had been previously in the wall.</p>

### 입력 

 <p>The first line is the number K of input data sets, followed by the K data sets, each of the following form:</p>

<p>The first line of the data set contains three integers n, s, p. The integer 1 ≤ n ≤ 1000 is the number of straight-line segments in the wall. 0 < s < 100 is the number of hours it takes one person to tear down one meter of wall. 1 ≤ p ≤ 1000 is the number of people tearing down the wall.</p>

<p>This is followed by n + 1 lines, each containing two integers x<sub>i</sub>, y<sub>i</sub> with −10000 ≤ x<sub>i</sub>, y<sub>i</sub> ≤ 10000. This is the i th point describing the wall. The i th segment of the wall runs from (x<sub>i</sub>, y<sub>i</sub>) to (x<sub>i+1</sub>, y<sub>i+1</sub>). As promised above, all wall pieces are horizontal or vertical, meaning that for each i, either x<sub>i+1</sub> = x<sub>i</sub> or y<sub>i+1</sub> = y<sub>i</sub>. Furthermore, we will ensure that the wall never crosses itself.</p>

### 출력 

 <p>For each data set, output “Data Set x:” on a line by itself, where x is its number.</p>

<p>Then output the number of hours it will take the p people to tear down the entire wall, rounded up to the nearest integer. (So if it would take 3.1 hours, you should output 4, not 3.)</p>

<p>Each data set should be followed by a blank line.</p>

