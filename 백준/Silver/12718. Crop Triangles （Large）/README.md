# [Silver I] Crop Triangles (Large) - 12718 

[문제 링크](https://www.acmicpc.net/problem/12718) 

### 성능 요약

메모리: 114488 KB, 시간: 128 ms

### 분류

조합론(combinatorics), 수학(math), 정수론(number_theory)

### 문제 설명

<p>Some pranksters have watched too much Discovery Channel and now they want to build a crop triangle during the night. They want to build it inside a large crop that looks like an evenly spaced grid from above. There are some trees planted on the field. Each tree is situated on an intersection of two grid lines (a grid point). The pranksters want the vertices of their crop triangle to be located at these trees. Also, for their crop triangle to be more interesting they want the <em>center</em> of that triangle to be located at some grid point as well. We remind you that if a triangle has the vertices (x<sub>1</sub>, y<sub>1</sub>), (x<sub>2</sub>, y<sub>2</sub>) and (x<sub>3</sub>, y<sub>3</sub>), then the center for this triangle will have the coordinates ((x<sub>1</sub> + x<sub>2</sub> + x<sub>3</sub>) / 3, (y<sub>1</sub> + y<sub>2</sub> + y<sub>3</sub>) / 3).</p>

<p>You will be given a set of points with integer coordinates giving the location of all the trees on the grid. You are asked to compute how many triangles you can form with <strong>distinct</strong>vertexes in this set of points so that their center is a grid point as well (i.e. the center has integer coordinates). </p>

<p>If a triangle has area 0 we will still consider it a valid triangle.</p>

### 입력 

 <p>The first line of input gives the number of cases, <strong>N</strong>. <strong>N</strong> test cases follow. Each test case consists of one line containing the integers <strong>n</strong>, <strong>A</strong>, <strong>B</strong>, <strong>C</strong>, <strong>D</strong>, <strong>x<sub>0</sub></strong>, <strong>y<sub>0</sub></strong> and <strong>M</strong> separated by exactly one space. <strong>n</strong> will be the number of trees in the input set. Using the numbers <strong>n</strong>, <strong>A</strong>, <strong>B</strong>, <strong>C</strong>, <strong>D</strong>, <strong>x<sub>0</sub></strong>, <strong>y<sub>0</sub></strong> and <strong>M</strong> the following pseudocode will print the coordinates of the trees in the input set. <em>mod</em> indicates the remainder operation.</p>

<p>The parameters will be chosen such that the input set of trees will not have duplicates.</p>

<pre><code><strong>X</strong> = <strong>x<sub>0</sub></strong>, <strong>Y</strong> = <strong>y<sub>0</sub></strong>
print <strong>X</strong>, <strong>Y</strong>
for i = 1 to <strong>n</strong>-1
  <strong>X</strong> = (<strong>A</strong> * <strong>X</strong> + <strong>B</strong>) mod <strong>M</strong>
  <strong>Y</strong> = (<strong>C</strong> * <strong>Y</strong> + <strong>D</strong>) mod <strong>M</strong>
  print <strong>X</strong>, <strong>Y</strong></code></pre>

<p>Limits</p>

<ul>
	<li>1 <= <strong>N</strong> <= 10, </li>
	<li>0 <= <strong>A</strong>, <strong>B</strong>, <strong>C</strong>, <strong>D</strong>, <strong>x<sub>0</sub></strong>, <strong>y<sub>0</sub></strong><= 10<sup>9</sup>, </li>
	<li>1 <= <strong>M</strong> <= 10<sup>9</sup>.</li>
	<li>3 <= <strong>n</strong> <= 100000.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #<strong>X</strong>: " where <strong>X</strong> is the test case number (starting from 1). This should be followed by an integer indicating the number of triangles which can be located at 3 distinct trees and has a center that is a grid point.</p>

