# [Silver III] I-Soar - 4728 

[문제 링크](https://www.acmicpc.net/problem/4728) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

자료 구조, 우선순위 큐, 스택

### 제출 일자

2025년 3월 24일 08:02:57

### 문제 설명

<p>The town meeting was not going well. ”It’s noisy”, some town residents complained. ”It’s ugly”, others stated. ”It’s an eyesore”, many agreed. ”It’s here,” said the mayor, ”and it’s not going to go away.”</p>

<p>The cause of all this furor was the new stretch of Interstate Highway that had been just opened. Straight as an arrow, it ran along the entire northern edge of the town.<br>
￼<br>
”Look,” said the mayor, ”we can reduce the noise and improve the view by planting trees and tall hedges along the road, but we don’t have an unlimited budget. Luckily, much of the highway is already hidden by some of the buildings in our commercial district on the north. We’ll see what we can do by planting in the visible gaps between the buildings.”</p>

<p>Write a program to compute the total linear length of planting that will be required to block the view of the Interstate by an observer looking straight north (orthogonal to the highway) from the southern side of the commercial district.</p>

### 입력 

 <p>Input consists of multiple data sets. The first line in each data set contains the length of the town border adjacent to the highway, expressed as a floating point number (called L, below). A nonpositive value for this number signals the end of input. This is followed by zero or more lines containing the positions of buildings within the commercial district. Each such line gives a pair of x positions (floating point numbers) representing the portion of the interstate whose view is occluded by the building. These numbers are expressed in the same units of measurement as the length of the border, such that 0 denotes the western end of the border and L the eastern end. The end of a data set is signaled by any pair x<sub>1</sub>, x<sub>2</sub> for which x<sub>1</sub> > x<sub>2</sub>.</p>

### 출력 

 <p>For each data set, print one line of the form</p>

<p>   The total planting length is ##</p>

<p>where ## is a floating point number, printed to one decimal place precision, denoting the total length of the Interstate visible between the buildings.</p>

